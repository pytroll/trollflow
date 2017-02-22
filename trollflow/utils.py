import importlib
import logging
from collections import OrderedDict
import Queue
import yaml

logger = logging.getLogger(__name__)


def get_class(clazz_path):
    parts = clazz_path.split('.')
    module_name = ".".join(parts[:-1])
    clazz_name = parts[-1]
    module = importlib.import_module(module_name)
    clazz = getattr(module, clazz_name)
    logger.info("Initialized %s", str(clazz))
    return clazz


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def stop_worker(worker):
    """Stop the given worker and join all the queues"""
    try:
        worker.stop()
    except AttributeError:
        pass
    try:
        # Make sure that all items have been cleared
        while worker.input_queue.unfinished_tasks > 0:
            logger.debug("%d unfinished task(s) in input queue",
                         worker.output_queue.unfinished_tasks)
            worker.input_queue.task_done()
            worker.input_queue.join()
    except AttributeError:
        pass


def get_data_from_worker(worker):
    """Read data from the output queue of the given worker."""
    if worker.output_queue is None:
        return None
    while True:
        try:
            data = worker.output_queue.get(True, 1)
            worker.output_queue.task_done()
            return data
        except Queue.Empty:
            continue
