#!/usr/bin/env python

from trollflow.workflow_launcher import WorkflowLauncher
import logging
import sys

logger = logging.getLogger(__name__)


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
