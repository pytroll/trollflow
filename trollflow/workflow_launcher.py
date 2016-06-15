import simplejson as json
import workflow_runner
import logging
from sys import argv

logger = logging.getLogger(__name__)


class WorkflowLauncher(object):

    format = '[%(levelname)s: %(asctime)s: %(name)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=format,
                        datefmt='%Y-%m-%d %H:%M:%S')

    def __init__(self, path_to_workflow):
        self.workflow = self.read_workflow(path_to_workflow)
        self.context = self.build_context(self.workflow)

    def run(self):
        runner = workflow_runner.WorkflowRunner(self.workflow)
        runner.run(self.context)

    def read_workflow(self, path_to_workflow):
        logger.info("Reading workflow {0}".format(path_to_workflow))
        try:
            wf_file = open(path_to_workflow, "r")
            wf_json_str = wf_file.read()
            return json.loads(wf_json_str)
        except Exception, e:
            raise e

    def build_context(self, json):
        logger.info("Constructing context.")

        context = {}
        components = json["Workflow"]

        for module, slots in sorted(components.items()):
            for slot_name, slot_details in slots.items():
                if not slot_name in context:
                    slot = {slot_name: {"content": None}}
                    if slot_details:
                        uri = slot_details["uri"]
                        slot[slot_name]["uri"] = uri
                    context.update(slot)
                else:
                    if slot_details:
                        uri = slot_details["uri"]
                        slot[slot_name]["uri"] = uri
                    context.update(slot)

        # add global configuration here
        if "global_config" in json.keys():
            if isinstance(json["global_config"], dict):
                context["global_config"] = json["global_config"]
            elif isinstance(json["global_config"], str):
                # trying to build a dict from configuration code...
                import utils
                global_config = utils.get_class(json["global_config"])
                context["global_config"] = global_config

        return context

if __name__ == '__main__':
    script, filename = argv

    logger.info("Launching workflow {0}".format(filename))
    wf = WorkflowLauncher(filename)
    wf.run()
