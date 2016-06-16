#!/usr/bin/env python

import yaml
from trollflow import workflow_runner
import logging
import sys

logger = logging.getLogger(__name__)


class WorkflowLauncher(object):

    def __init__(self, path_to_workflow):
        self.workflow = self.read_workflow(path_to_workflow)
        self.context = self.build_context(self.workflow)

    def run(self):
        runner = workflow_runner.WorkflowRunner(self.workflow)
        runner.run(self.context)

    def read_workflow(self, path_to_workflow):
        logger.info("Reading workflow {0}".format(path_to_workflow))
        with open(path_to_workflow, "r") as fid:
            config = yaml.safe_load(fid)
        return config

    def build_context(self, config):
        logger.info("Constructing context.")

        context = {}
        components = config["Workflow"]

        for component in components:
            module, slots = component.items()[0]
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
        if "global_config" in config.keys():
            if isinstance(config["global_config"], dict):
                context["global_config"] = config["global_config"]
            elif isinstance(config["global_config"], str):
                # trying to build a dict from configuration code...
                from trollflow import utils
                global_config = utils.get_class(config["global_config"])
                context["global_config"] = global_config

        return context

def main():
    logger = logging.getLogger('workflow_yaml_launcher')

    fmt = '[%(levelname)s: %(asctime)s: %(name)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=fmt,
                        datefmt='%Y-%m-%d %H:%M:%S')

    filename = sys.argv[1]

    logger.info("Launching workflow {0}".format(filename))
    wf_ = WorkflowLauncher(filename)
    wf_.run()

if __name__ == '__main__':
    main()
