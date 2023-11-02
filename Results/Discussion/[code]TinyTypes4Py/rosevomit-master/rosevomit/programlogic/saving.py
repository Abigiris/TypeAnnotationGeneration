# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# saving.py
# rosevomit.programlogic.saving
# ___________________________________________________________________
"""This file handles Rosevomit's filesaving behavior."""
from typing import Callable
from core import logs
import core.utilities as ut
from programcli import dialogsave


_SAVELOGGER = logs.BaseLogger (__name__)

# TODO: This entire module is incomplete and not used.

# Generic save function
def generic_save_results(ARG_function: Callable, ARG_filetype: str="txt"):
    """Asks the user to see if they want to save the results of a function, and proceeds accordingly."""
    do_we_save: bool = dialogsave.prompt_save_yesno()
    if do_we_save is False:
        ARG_function()
    else:
        pass

# Generic save function
def generic_save_changes():
    """NOT YET IMPLEMENTED. Asks the user if they want to save changes to a file, and proceeds accordingly."""
    raise NotImplementedError

# ---------- Feature-specific save functions ----------
def save_names():
    """NOT YET IMPLEMENTED. Handles the save logic for random name generation."""
    raise NotImplementedError


def save_timeline():
    """NOT YET IMPLEMENTED. Handles the save logic for random timeline generation."""
    raise NotImplementedError


def save_suncalculations():
    """NOT YET IMPLEMENTED. Handles the save logic for suncalc."""
    raise NotImplementedError
