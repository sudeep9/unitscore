
import logging
import units.coreunits as coreunits
import units.utils

log = logging.getLogger(__name__)

class Engine:
    def __init__(self, config):
        self.config = config
        self.flowname = None
        self.context = None


    def __getUnit(self, instconfig):
        unitname = instconfig['name']
        funcname = self.config.units[unitname]['function']
        func = units.utils.importClass(funcname)
        return func

    def __runflow(self, flowname):
        self.flowname = flowname

        self.context = dict()
        self.context['flowname'] = self.flowname
        self.context['config'] = self.config

        if not coreunits.unit_checkFlowConfig(self.context):
            return False

        flowunits = self.config.flows[self.flowname]['units']
        unitsorder = self.config.flows[self.flowname]['order']

        for inst in unitsorder:
            print "\n", inst
            print "----------------------------------------"
            func = self.__getUnit(flowunits[inst])
            if not func(self.context):
                log.error("Flow instance '%s' failed", inst)
                return False

        return True
        

    def run(self, flowname):
        log.info("running flow: %s", flowname)

        result = self.__runflow(flowname)

        return result
