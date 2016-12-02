import glob2
import ast
import logging
import os
import sys

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


def main():
    """Main()"""
    pathname = sys.argv[0]

    logger.info("Findging components in %s", pathname)
    finder = ComponentFinder(pathname)
    finder.run()

if __name__ == '__main__':
    main()
