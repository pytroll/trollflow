from trollflow.workflow_component import AbstractWorkflowComponent
from PIL import Image


class Writer(AbstractWorkflowComponent):

    def pre_invoke(self):
        pass

    def invoke(self, context):
        """Write a GIF file's contents."""
        try:
            img = Image.fromarray(context[self.slots[0]]["uri"], 'w')
            img.save(context[self.slots[0]]["content"])
        except Exception as err:
            raise err

    def post_invoke(self):
        pass
