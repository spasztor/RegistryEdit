# A utility designed to alter the following registries to the corresponding values:
#!/usr/bin/env python

__author__ = "Szabolcs Pasztor"
__copyright__ = "Copyright 2014, The Cogent Project"
__credits__ = "Szabolcs Pasztor"
__license__ = "GPL"
__version__ = "1.0.2"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "spasztor@GoldsmithEngineering.com"
__status__ = "Deployment"

import logging
import time
import winreg

# Logging setup:
_LOG_FILE_NAME = "error.log" 
logging.basicConfig(filename = _LOG_FILE_NAME, filemode = 'a', level = logging.DEBUG)

# The following is a series of definitions dependent on the version of AutoCad being used:
_ACAD_VERSIONS = ["2014", "2015"]
_ACAD_VERSION = "2015" # Change to match target AutoCad Version
_KEY_LOCATIONS = {_ACAD_VERSIONS[0] : "\\R19.1\\ACAD-D000:409", _ACAD_VERSIONS[1] : "\\R20.0\\ACAD-E000:409"}
_KEY_LOCATION = ("Software\\Autodesk\\AutoCAD" + _KEY_LOCATIONS[_ACAD_VERSION]
                         + "\\Profiles\\c3d\General")

def main():
    # Main Driver for utility

    # Create a connection to _KEY_LOCATION and open registry key for editing:
    connected_registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    open_key = winreg.CreateKeyEx(connected_registry, _KEY_LOCATION, access=winreg.KEY_ALL_ACCESS)

    # Set sub-key values:
    winreg.SetValueEx(open_key, "PrinterStyleSheetDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plot Styles")
    winreg.SetValueEx(open_key, "PrinterConfigDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plotters")
    winreg.SetValueEx(open_key, "PrinterDescDir", 0, winreg.REG_SZ, "S:\\Publish Settings\\Plotters\\PMP Files")
    winreg.SetValueEx(open_key, "DefaultConfig", 0, winreg.REG_SZ, "Oce PlotWave 750 Overwrite.pc3")
    winreg.SetValueEx(open_key, "HideSystemPrinters", 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(open_key, "PlotOffset", 0, winreg.REG_DWORD, 1)

    # Close Registry
    winreg.CloseKey(connected_registry)

try:
    main()
except:
    logging.exception(time.strftime("%d/%m/%Y") + "; " + time.strftime("%I:%M:%S") + "Exception thrown.")

logging.shutdown()