# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# startup.py
# rosevomit.core.startup
# ___________________________________________________________________
"""The setup utility file for Alex's "Project ROSEVOMIT", a random name generator  and random timeline generator written in Python."""
from core import logs
from core.constants import MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION, IS_DEVBUILD
from core.utilities import debugmessage
from programcli import messages

_STARTUPLOGGER = logs.BaseLogger(__name__)

def main_setup ():
    """Contains setup instructions, and prints that info to terminal. Accepts no parameters, returns nothing."""
    _STARTUPLOGGER.logger.debug ("Starting main setup procedure.")
    print()

    if int (MAJOR_VERSION) >= 1 and IS_DEVBUILD:
        messages.warning_version_is_devbuild()
    elif int (MAJOR_VERSION) < 1:
        if IS_DEVBUILD:
            messages.warning_version_is_prerelease_devbuild (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)
        else:
            messages.warning_version_is_prerelease (MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)

    messages.general_program_message ("Press any key to accept risk and continue, or end the program by exiting this window.")
    debugmessage ("Main setup complete.")
    _STARTUPLOGGER.logger.info ("Finished main setup procedure.")
