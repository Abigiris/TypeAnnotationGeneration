# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# exiting.py
# rosevomit.programlogic.exiting
# ___________________________________________________________________
"""This file handles Rosevomit's exiting behavior."""
import sys

from core import logs, settings, tempfiles
from programcli import dialogexit

EXITLOGGER = logs.BaseLogger (__name__)

def exit_rosevomit():
    """Handles Rosevomit's exit behavior. Accepts nothing, returns nothing."""
    do_temp_files_exist: bool = not tempfiles.is_empty()  # The 'not' operator effectively reverses the boolean returned from tempfiles.is_empty()
    always_show_exit_dialog: bool = settings.exit_dialog()
    autoclean_temp_directory: bool = settings.autoclean_temp_directory()

    if do_temp_files_exist is True and autoclean_temp_directory is True:
        tempfiles.delete()

    if always_show_exit_dialog is True:
        dialogexit.simple_exit_dialog()  # "Are you sure you want to exit?"
    else:
        EXITLOGGER.logger.critical ("Exiting ROSEVOMIT.")
        sys.exit(0)
