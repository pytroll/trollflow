import glob2
import ast
import logging
import os
from sys import argv

logger = logging.getLogger(__name__)


class ComponentFinder(object):

    format = '[%(levelname)s: %(asctime)s: %(name)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=format,
                        datefmt='%Y-%m-%d %H:%M:%S')

    def __init__(self, pathname):
        self.search_path = pathname

    def run(self):
        # find Python files
        components = []
        files = glob2.glob("{0}/**/*.py".format(self.search_path))
        for py_file in files:
            with open(py_file) as py_code:
                py_code = py_code.read()
                py_ast = ast.parse(py_code)
                possibble_classes = [node for node in ast.walk(py_ast)
                                     if isinstance(node, ast.ClassDef)]
                # AbstractWorkflowComponent
                component_classes = [node.name for node in possibble_classes
                                     if "AbstractWorkflowComponent"
                                     in node.bases[0].id]
                if component_classes:
                    print os.path.abspath(py_file)
                    components.append(os.path.abspath(py_file))

        return components

if __name__ == '__main__':
    script, pathname = argv

    logger.info("Findging components in {0}".format(pathname))
    finder = ComponentFinder(pathname)
    finder.run()



# j =ast.parse("""class OI(object):
#     pass""")
#   16: j
#   17: j.body
#   18: i = j.body
#   19: ast.ClassDef
#   20: j
#   21: dump(j)
#   22: ast.dump(j)
#   23: classes = [node.name for node in ast.walk(j) if isinstance(node, ast.ClassDef)]
#   24: classes
#   25: classes = [node for node in ast.walk(j) if isinstance(node, ast.ClassDef)]
#   26: classes
#   27: classes = [node.bases for node in ast.walk(j) if isinstance(node, ast.ClassDef)]
#   28: classes
#   29: classes = [node.name for node in ast.walk(j) if isinstance(node, ast.ClassDef) and node.bases.Name]
#   30: classes = [node.name for node in ast.walk(j) if isinstance(node, ast.ClassDef) and node.bases.Name[0].id == "OI"]
#   31: dump(j)
#   32: ast.dump(j)
#   33: %history -g
