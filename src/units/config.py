

import os

# Technical settings for units
#==================================================================

logpath = os.environ['HOME']

# The core units & flows are configured here
#==================================================================

# The dict where all the flows are configured
flows = {}

# The dict where all the units are registered
units = {}


# The core units & flows are configured here
#==================================================================

units = {
    "Parse input args" : {
        "function" : "units.coreunits.unit_parseArgs"
    },
    "Check flow config" : {
        "function" : "units.coreunits.unit_checkFlowConfig"
    },
    "Check all flow config" : {
        "function" : "units.coreunits.unit_checkAllFlowConfig"
    },
}


flows['configcheck'] = {
    "order" : ['Check flows', 'Parse args'],
    "units" : {
        "Parse args" : {
            "name"    : "Parse input args",
            "argspec" : [
                #name    , action , nargs, const, default, type, choices                  , required, help              , metavar, dest
                ('--mode', 'store', None , None , 'all'  , None, ['all', 'units', 'flows'], None    , "aspects to check", None   , None)    
            ],
        },
        "Check flows" : {
            "name" : "Check all flow config"
        }
    },
}

flows['sample'] = {
    "units" : {
        "Check flows" : {
            "name" : "Check all flow config"
        }
    },
}
