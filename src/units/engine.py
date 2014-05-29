
import logging
import units.coreunits as coreunits
import units.utils

log = logging.getLogger(__name__)

class Engine:
    def __init__(self, config):
        self.config = config
        self.flowname = None
        self.context = None


    def __getunit(self, instconfig):
        unitname = instconfig['name']
        funcname = self.config.units[unitname]['function']
        func = units.utils.importClass(funcname)
        return func

    def __rununit(self, unit):
        result = unit(self.context)

        return result

    def __setUnitContext(self, unitInstConfig):
        self.context['currentunit'] = unitInstConfig

    def __runflow(self, flowname, args):

        #1: Setup the context and initialize
        #-------------------------------------------
        self.flowname = flowname
        self.context = dict()
        self.context['flowname'] = self.flowname
        self.context['config'] = self.config
        self.context['stack'] = list()
        self.context['input'] = dict()
        self.context['input']['args'] = args

        #2: Verify the flow config
        #-------------------------------------------
        if not coreunits.unit_checkFlowConfig(self.context):
            return False

        #3: Start executing
        #-------------------------------------------
        flowunits = self.config.flows[self.flowname]['units']
        unitsorder = self.config.flows[self.flowname]['order']

        for inst in unitsorder:
            print "\n", inst
            print "----------------------------------------"

            instconfig = flowunits[inst]
            func = self.__getunit(instconfig)
            self.__setUnitContext(instconfig)

            if not self.__rununit(func):
                log.error("Flow instance '%s' failed", inst)
                return False

            self.context['stack'].append(inst)

        return True
        

    def run(self, flowname, args):
        log.info("running flow: %s", flowname)

        result = self.__runflow(flowname, args)

        return result
