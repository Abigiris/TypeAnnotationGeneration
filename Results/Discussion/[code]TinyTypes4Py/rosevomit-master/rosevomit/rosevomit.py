# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# rosevomit.py
# rosevomit.programlogic.rosevomit
# ___________________________________________________________________
"""The main file for Alex's "Project ROSEVOMIT", a random name generator and random timeline generator written in Python."""
import sys
import textwrap

# INTERNAL MODULES
import core  # <-- Keep this as the first internal import! Logging is started by the __init__.py of the core module
from core import settings, startup
from core.constants import SEE_ROSA_RUN
from programcli import worsecli


MAINLOGGER = core.logs.BaseLogger(__name__)
print ()
print ("Starting ROSEVOMIT.")
MAINLOGGER.logger.critical ("Starting ROSEVOMIT.")

if settings.existence() is False:
    print ("The settings don't exist. Recreating settings file at:")
    print (f"  {settings.SETTINGS_FILE}")
    settings.restore_file()
    print ()
elif settings.is_valid() is False:
    print (textwrap.fill ("WARNING: The settings file seems to be corrupted. Rosevomit will restore it to its default state. Press enter to continue. If you do not wish to overwrite the current settings file, please close the program now without pressing enter."))
    input ()
    settings.restore_file()
else:
    pass

MAINLOGGER.logger.debug ("Calling main setup...")
startup.main_setup()

MAINLOGGER.logger.debug ("Displaying main menu for the first time...")
print ()
print (69 * "-")
print (27 * "-", "ROSEVOMIT.PY", 28 * "-")
print (69 * "-")
print ()

# After setup, rosevomit.py will display the main menu and will carry out instructions based on user input. This is an infinite loop - if rosevomit.py ever has no more instructions to carry out, it displays the main menu again and awaits further instructions. This is based on the 'SEE_ROSA_RUN' variable. This variable should never change. If it does, the program exits and gives the system an error code.
worsecli.show_main_menu()
while SEE_ROSA_RUN is True:
    try:
        worsecli.ask_for_input()
    except Exception as problem:  # pylint: disable=broad-except
        print (problem)
        print ()
        print (problem.__traceback__)
        input()
sys.exit(1)
