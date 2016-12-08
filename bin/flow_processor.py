#!/usr/bin/env python

"""Main script for trollflow based processors."""

import logging
import logging.config
import sys
import time

from trollflow.workflow_streamer import WorkflowStreamer
from trollflow.utils import ordered_load


def generate_daemon(config_item):
    """Return a daemon based on the YAML configuration"""
    return config_item['components'][-1]['class']


def generate_thread_workflow(config_item):
    wfs = WorkflowStreamer(config=config_item)
    wfs.start()
    return wfs


TYPES = {'daemon': generate_daemon,
         'workflow': generate_thread_workflow,
         'thread_workflow': generate_thread_workflow, }


def read_yaml_config(fname):
    """Read YAML config file"""
    # Read config
    with open(fname, "r") as fid:
        config = ordered_load(fid)

    return config


def setup_logging(config):
    """Setup logging"""

    # Check if log config is available, use it if it is
    for item in config["config"]:
        if "log_config" in item.keys():
            logging.config.fileConfig(item["log_config"],
                                      disable_existing_loggers=False)


def create_workers(config):
    """Create workers"""

    workers = []

    for item in config['work']:
        workers.append(TYPES[item['type']](item))

    queue = None
    for worker in workers:
        if queue is not None:
            worker.input_queue = queue
        try:
            queue = worker.output_queue
        except AttributeError:
            queue = worker.queue

    return workers


def wait(workers, logger):
    """Loop workers until keyboard interrupt is detected, after which join
    the queues and stop the worker instances."""
    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Closing flow processing items")
            for worker in workers:
                worker.stop()
                try:
                    # Make sure that all items have been cleared
                    while worker.input_queue.unfinished_tasks > 0:
                        logger.debug("%d unfinished task in input queue",
                                     worker.output_queue.unfinished_tasks)
                        worker.input_queue.task_done()
                    worker.input_queue.join()
                except AttributeError:
                    pass
                try:
                    # Make sure that all items have been cleared
                    while worker.output_queue.unfinished_tasks > 0:
                        logger.debug("%d unfinished task in output queue",
                                     worker.output_queue.unfinished_tasks)
                        worker.output_queue.task_done()
                    worker.output_queue.join()
                except AttributeError:
                    pass

            break


def main():
    """Main()"""

    config = read_yaml_config(sys.argv[1])

    setup_logging(config)
    logger = logging.getLogger("flow_processor")
    logger.info("Initializing flow processor")

    workers = create_workers(config)

    logger.info("Ready to process new data")

    wait(workers, logger)

    logger.info("Flow processor has been shutdown.")

if __name__ == "__main__":
    main()
