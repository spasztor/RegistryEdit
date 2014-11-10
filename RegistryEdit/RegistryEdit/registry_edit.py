"""
A utility designed to alter the following registries to the corresponding values:
"""

#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "spasztor@GoldsmithEngineering.com"
__status__ = "Production"

import logging
import os
import time
import sys
import winreg


_LOG_FILE_NAME = "traceback.log" 
logging.basicConfig(filename = _LOG_FILE_NAME, filemode = 'a', level = logging.DEBUG)

""" The following is a definition of various locations depended on the version of AutoCad being used. """
_ARGUMENTS = ["/2014", "/2015"]
_KEY_LOCATIONS = {_ARGUMENTS[0] : "\\R19.1\\ACAD-D000:409", _ARGUMENTS[1] : "\\R20.0\\ACAD-E000:409"}

if len(sys.argv) > 1 and sys.argv[1] in _ARGUMENTS:
    _VERSION = sys.argv[1]
else:
    _VERSION = "/2015"

_KEY_LOCATION = ("Software\\Autodesk\\AutoCAD" + _KEY_LOCATIONS[_VERSION]
                         + "\\Profiles\\c3d\General")

def main():
    # Main Driver for utility
    connected_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    open_key = winreg.CreateKeyEx(connected_registry, _KEY_LOCATION, access=winreg.KEY_ALL_ACCESS)

    winreg.SetValueEx(open_key, "PrinterStyleSheetDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plot Styles")
    winreg.SetValueEx(open_key, "PrinterConfigDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plotters")
    winreg.SetValueEx(open_key, "PrinterDescDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plotters\\PMP Files")
    winreg.SetValueEx(open_key, "DefaultConfig", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plotters 2014\\Old Plotters\\Oce PlotWave 750.pc3")
    winreg.SetValueEx(open_key, "HideSystemPrinters", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(open_key, "PlotOffset", 0, winreg.REG_DWORD, 1)

    winreg.CloseKey(connected_registry)

try:
    main()
except:
    logging.exception(time.strftime("%d/%m/%Y") + "; " + time.strftime("%I:%M:%S")) + "Exception thrown."

logging.shutdown()