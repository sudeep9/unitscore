#!/usr/bin/env python

import sys
import os.path
import logging
import datetime

abspath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(abspath + "/../src")

import units.utils
import units.engine



def setupLogging(config, flowname):
    formatter = logging.Formatter("-" * 80 + "\n%(asctime)s : %(name)s (%(lineno)s) : %(funcName)s\n%(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")

    timestamp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
    logfilename = "units_{0}_{1}.log".format(flowname, datetime.datetime.today().strftime('%Y%m%d_%H%M%S'))
    fullLogfile = config.logpath + "/{0}".format(logfilename)

    print "*Log file: {0}".format(fullLogfile)

    fh = logging.FileHandler(fullLogfile, mode = "w")
    fh.setFormatter(formatter)
    #fh.setLevel(getattr(logging, args.loglevel.upper(), None)) 
    fh.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)
    logger.addHandler(fh)
    #logger.setLevel(getattr(logging,args.loglevel.upper(), None)) 
    logger.setLevel(logging.INFO)

    logger.debug("Logging setup done")
    logger.info("log path: " + config.logpath)
    logging.getLogger("units").addHandler(fh)
    #logging.getLogger("auror").setLevel(getattr(logging,args.loglevel.upper(), None))
    logging.getLogger("units").setLevel(logging.INFO)


def usage():
    print "Usage: "
    print "   %s <config> <flowname> [options]" % sys.argv[0]


def loadConfig(configname):
    return units.utils.loadConfig(configname)

if __name__ == "__main__":

    if len(sys.argv[2:]) < 1:
        print "Error: not enough arguments"
        usage()
        exit(1)


    configname, flowname = sys.argv[1], sys.argv[2]

    config = loadConfig(configname)
    setupLogging(config, flowname)

    engine = units.engine.Engine(config)
    if engine.run(flowname, sys.argv):
        print "Flow '%s' finished with success" % flowname
    else:
        print "Flow '%s' finished with error" % flowname
        exit(1)


   
