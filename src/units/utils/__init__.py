
import importlib
import logging

log = logging.getLogger(__name__)

def importClass(name):
    # name is assumed to be like: auror.product.enaber75.EnablerEnvironment
    # Split the module name by the dot(.)

    parts = name.split('.')

    # if there are no dots then 'parts' will be a an array of 1 element
    # If this is the case then the class should be in the current module
    if len(parts) > 1:
        module = importlib.import_module(".".join(parts[:-1]))
    else:
        module = None

    if module is not None:
        loadedClass = getattr(module, parts[-1])
    else:
        #loadedClass = globals()[parts[-1]]
        loadedClass = None
        localmodule = inspect.getmodule(inspect.currentframe().f_back)
        loadedClass = getattr(localmodule, parts[-1])
    return loadedClass


def loadConfig(requestedConfig):

    if requestedConfig == 'core':
        configname = 'units.config'
    else:
        configname = requestedConfig

    config = importlib.import_module(configname)
    return config
