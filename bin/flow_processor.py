#!/usr/bin/env python

"""Main script for trollflow based processors."""

import logging
import logging.config
import sys
import time
from Queue import Queue

from trollflow.workflow_streamer import WorkflowStreamer
from trollflow.utils import ordered_load, stop_worker, get_data_from_worker


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
    if "log_config" in config["config"]:
        logging.config.fileConfig(config["config"]["log_config"],
                                  disable_existing_loggers=False)


def create_threaded_workers(config):
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


def wait_threads(workers, logger):
    """Loop workers until keyboard interrupt is detected, after which join
    the queues and stop the worker instances."""
    while True:
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            logger.info("Closing flow processing items")
            for worker in workers:
                stop_worker(worker)
            break


def run_serial_flow(config, logger):
    """Run processing in serial.  Daemons are still in their own threads,
    but workflow items are run in sequence."""

    logger.info("Creating daemons and collecting workflow items")

    workers = []

    # Create daemons and collect workers
    for item in config['work']:
        if item["type"] == 'daemon':
            workers.append({"daemon": TYPES['daemon'](item)})
        else:
            workers.append({'workflow': item})

    data = None
    while True:
        try:
            for item in workers:
                # Create a workflow object.  Daemons are already
                # running, so those can be skipped here
                if "workflow" in item:
                    worker = generate_thread_workflow(item["workflow"])
                else:
                    worker = item["daemon"]

                # If there's no data, try to get some
                if data is None:
                    data = get_data_from_worker(worker)
                    # Stop workflow object
                    if "workflow" in item:
                        stop_worker(worker)
                    # Continue to the next worker and feed the new data to it
                    continue
                if worker.input_queue is None:
                    worker.input_queue = Queue()
                worker.input_queue.put(data)
                data = get_data_from_worker(worker)
                if "workflow" in item:
                    stop_worker(worker)

        except KeyboardInterrupt:
            for worker in workers:
                if "daemon" in worker:
                    stop_worker(worker["daemon"])
            return


def main():
    """Main()"""

    config = read_yaml_config(sys.argv[1])

    setup_logging(config)
    logger = logging.getLogger("flow_processor")
    logger.info("Initializing flow processor")

    use_threads = config["config"].get('use_threading', True)

    if use_threads:
        logger.debug("Using threaded processing")
        workers = create_threaded_workers(config)
        logger.info("Ready to process new data")
        wait_threads(workers, logger)
    else:
        logger.debug("Using serial processing.")
        run_serial_flow(config, logger)

    logger.info("Flow processor has been shutdown.")

if __name__ == "__main__":
    main()
