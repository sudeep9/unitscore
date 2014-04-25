

import logging

log = logging.getLogger(__name__)

def unit_parseArgs(ctx):
    print "Parsing args"


def unit_checkFlowConfig(ctx):
    flowname, config = ctx['flowname'], ctx['config']

    if flowname not in config.flows:
        log.error("flow '%s' not found in configuration", flowname)
        return False

    flowconfig = config.flows[flowname]

    if 'units' not in flowconfig:
        log.error("For flow '%s', no units specified", flowname)
        return False

    if 'order' not in flowconfig:
        log.error("For flow '%s', no order specified", flowname)
        return False

    flowunits = flowconfig['units']

    for unitinst in flowconfig['order']:
        if unitinst not in flowunits:
            log.error("For flow '%s', unit instance %s not defined in flow units", flowname, unitinst)
            return False

    for instname, instconfig in flowunits.iteritems():
        if 'name' not in instconfig:
            log.error("For flow '%s', unit instance '%s', unit 'name' not specified", flowname, instname)
            return False

        if instconfig['name'] not in config.units:
            log.error("For flow '%s', unit instance '%s', unit name '%s' not found in the configuration", flowname, instname, instconfig['name'])
            return False
        

    return True


def unit_checkAllFlowConfig(ctx):
    flowname, config = ctx['flowname'], ctx['config']
    allok = True

    for fname in config.flows:
        ctx['flowname'] = fname
        if not unit_checkFlowConfig(ctx):
            allok = False
            print "Flow %-20s - failed" % fname
            log.error("Flow %s failed in config check", fname)
        else:
            print "Flow %-20s - ok" % fname

    return allok
