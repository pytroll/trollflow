import importlib
import logging
import yaml
from yaml.constructor import ConstructorError
from collections import OrderedDict

logger = logging.getLogger(__name__)


def get_class(clazz_path):
    parts = clazz_path.split('.')
    module_name = ".".join(parts[:-1])
    clazz_name = parts[-1]
    module = importlib.import_module(module_name)
    clazz = getattr(module, clazz_name)
    logger.info("Initialized {0}".format(clazz))
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
