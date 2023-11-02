# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# settings.py
# rosevomit.core.settings
# ___________________________________________________________________
# pylint: disable=global-statement
"""This file checks handles interactions with the program settings. The program settings are *not* stored in this file, however - they are stored in settings-data.ini."""
import configparser
import os
import textwrap
from typing import Union

from core import logs

_SETTINGSLOGGER = logs.BaseLogger (__name__)

# ---------- Contents ----------
# ---------- -------- ----------
# This module has four subsections:
#   1. "Meta" functions (for handling the settings-data.ini file itself)
#   2. Functions for reading settings
#   3. Helper functions for displaying the settings dialog (used by the function in section 5)
#   4. The main function for displaying the settings dialog to the user

# This is an "always relative to this module" filepath
SETTINGS_FILE = os.path.join (os.path.dirname (__file__), "settings-data.ini")

# ---------- (1) "META" FUNCTIONS ----------
# These functions deal with the actual existence of the settings-data.ini file, and the recreation of it if necessary.
def existence() -> bool:
    """Checks to see if the file defined as the global constant SETTINGS_FILE exists.

    Returns
    -------
    bool
        Returns os.path.isfile(SETTINGS_FILE)

    Note
    ----
    This function might have trouble locating the SETTINGS_FILE if run as a module.
    """
    _result = os.path.isfile(SETTINGS_FILE)
    return _result


def is_valid() -> bool:
    """Checks to see if the file specified as the 'SETTINGS_FILE' has certain expected options and values.

    Returns
    -------
    bool
        Returns 'False' if core.settings.show_debug(), core.settings.logging_service(), core.settings.exit_dialog(), or core.settings.autoclean_temp_directory() raise configparser.Error.
    """
    try:
        show_debug()
        logging_service()
        exit_dialog()
        autoclean_temp_directory()
    except configparser.Error:
        return False
    else:
        return True


def restore_file():
    """Recreates the file specified in the 'SETTINGS_FILE' variable using internally defined defaults. Accepts no parameters, returns nothing."""
    # Initializing ConfigParser()
    config = configparser.ConfigParser(allow_no_value=True)
    # Entering the default values we want to restore
    # (Also, not that "'; this is a comment': None" is the way to insert comments into the auto-generated config file)
    config["debugging"] = {
        "show_debug": "off",
        "; ^ Should debug messages be printed to the console? Defaults to 'off'.": None,
        "logging_service": "on",
        "; Should debug messages be entered into a log? Defaults to 'on'.": None,
        }
    config["directories"] = {
        "; ^ (NOT YET IMPLEMENTED) Will allow users to specify custom locations to be used as /temp or /saved directories.": None,
    }
    config["exit behavior"] = {
        "exit_dialog": "off",
        "; ^ Displays a 'Are you sure you want to exit?' prompt before exiting. Defaults to 'off'.": None,
        "autoclean_temp_directory": "on",
        "; ^ Automatically deletes the contents of the /temp directory before exiting. Defaults to 'on'.": None,
        }
    # Creating the file
    with open(SETTINGS_FILE, "w+") as newfile:
        # Writing header comment
        newfile.write("; rosevomit/core/settings/settings-data.ini\n")
        newfile.write("; a file storing Rosevomit's settings\n")
        newfile.write("\n")
        # Writing default values
        config.write(newfile)

# ---------- (2) FUNCTIONS FOR READING SETTINGS ----------
# These functions are used for reading the values of settings from the settings file, either for display to the user or for internal program use.
# For developer readibility, these functions should be listed below in the same order that the values they read in the settings-data.ini file are listed.
def show_debug() -> bool:
    """Returns true or false based on the value of 'show_debug' in the 'settings-data.ini' file.

    Returns
    -------
    bool
        The return value of config.getboolean() for section 'debugging' and option 'show_debug'.
    """
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean (section="debugging", option="show_debug")
    return result


def logging_service() -> bool:
    """Returns true of false based on the value of 'logging_service' in the 'settings-data.ini' file.

    Returns
    -------
    bool
        The return value of config.getboolean() for section 'debugging' and option 'logging_service'.
    """
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean (section="debugging", option="logging_service")
    return result


def exit_dialog() -> bool:
    """Returns true or false based on the value of 'exit_dialog' in the 'settings-data.ini' file.

    Returns
    -------
    bool
        The return value of config.getboolean() for section 'exit behavior' and option 'exit_dialog'.
    """
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean (section="exit behavior", option="exit_dialog")
    return result


def autoclean_temp_directory() -> bool:
    """Returns true or false based on the value of 'autoclean_temp_directory' in the 'settings-data.ini' file.

    Returns
    -------
    bool
        The return value of config.getboolean() for section 'exit behavior' and option 'autoclean_temp_directory'.
    """
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()  # Create an instance of ConfigParser
    config.read_file(settings)
    result: bool = config.getboolean (section="exit behavior", option="autoclean_temp_directory")
    return result

# ---------- (3) HELPER FUNCTIONS FOR DISPLAYING SETTINGS DIALOG ----------
def prompt_to_change_settings() -> bool:
    """Asks the user if they want to change any settings.

    Returns
    -------
    bool
        If user inputs 'y', return 'True'. If user inputs 'n' or nothing, return 'False'.
    """
    _input = input ("Would you like to change any settings? y/[n]: ")
    _input = _input.strip()
    if _input in ("n", ""):
        return False
    elif _input == "y":
        return True
    else:
        print (f"Sorry, {_input} is not a valid option. Please enter 'y' or 'n'.")
        recursive_response = prompt_to_change_settings()
        return recursive_response


def _prompt_for_section_name (ARG_config_object: configparser.ConfigParser) -> Union[str, None]:
    """Prompts the user to enter a valid section name. Checks that section name exists.

    Parameters
    ----------
    ARG_config_object : configparser.ConfigParser
        The settings, which have been read from `SETTINGS_FILE` by configparser and stored in this configparser.ConfigParser object.


    Returns
    -------
    str or None
        If a string, it's an section name that exists in the given config object. If None, the user wishes to exit whatever dialog called this function.
    """
    print ()
    print ("Type the section name of the setting you would like to change, or")
    _input = input ("leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return None
    section_name = _input.lower()
    if ARG_config_object.has_section (section_name) is False:
        print (f"Sorry, {section_name} is not a valid section name.")
        recursive_result = _prompt_for_section_name (ARG_config_object)
        return recursive_result
    else:
        return section_name


def _prompt_for_option_name (ARG_config_object: configparser.ConfigParser, ARG_section: str) -> Union[str, None]:
    """Prompts the user to enter a valid option name. Checks that option name exists.

    Parameters
    ----------
    ARG_config_object : configparser.ConfigParser
        The settings, which have been read from `SETTINGS_FILE` by configparser and stored in this configparser.ConfigParser object.
    ARG_section : str
        A valid section name in the config object (see above).

    Returns
    -------
    str or None
        If a string, it's an option name that exists in the given section and config object. If None, the user wishes to exit whatever dialog called this function.
    """
    print ()
    print (f"SELECTED SECTION: {ARG_section}")
    print ("Type the option name of the setting you would like to change, or")
    _input = input ("leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return None
    option_name = _input.lower()
    if ARG_config_object.has_option (ARG_section, option_name) is False:
        print (f"Sorry, {option_name} is not a valid option name.")
        recursive_result = _prompt_for_option_name(ARG_config_object , ARG_section)
        return recursive_result
    else:
        return option_name


def _prompt_for_new_value (ARG_section: str, ARG_option: str) -> Union[str, None]:
    """Prompts the user to enter a new value.

    Unlike the other '_prompt_ functions, we don't need an argument for the ConfigParser object becasuse we aren't using using any of its validation methods.

    Parameters
    ----------
    ARG_section : str
        A valid section name in the ConfigParser object.
    ARG_option : str
        A valid option name in the ConfigParser object.

    Returns
    -------
    str or None
        If a string, it's the value the user entered. If None, the user wishes to exit whatever dialog called this function.
    """
    print ()
    print (f"SELECTED SECTION: {ARG_section}, SELECTED OPTION: {ARG_option}")
    _input = input ("Type the desired new value, or leave blank to exit: ")
    _input = _input.strip()
    if _input == "":
        return None
    else:
        new_value = _input
        return new_value



def dialog_change_setting():
    """Asks the user to type the name of the setting they wish to change. Validates that the user's input is an actual name ('key') in the 'settings-data.ini' file. Launches the appropriate function to change that setting. Accepts no parameters, returns nothing."""
    global SETTINGS_FILE
    settings = open (SETTINGS_FILE)
    config = configparser.ConfigParser()
    config.read_file(settings)

    section: str = _prompt_for_section_name (config)
    if section is None:
        return
    option: str = _prompt_for_option_name (config, section)
    if option is None:
        return
    value: str = _prompt_for_new_value (section, option)
    if value is None:
        return
    config.set (section, option, value)
    settings = open (SETTINGS_FILE, "w")
    config.write (settings)
    print (f"Option {option} in section {section} was set to {value}")
    print()


# ---------- (4) MAIN FUNCTION FOR DISPLAYING SETTINGS DIALOG ----------
# NOTE: Perhaps this should go in the programcli folder? Need to think about it.
def settings_user_interface (ARG_show_header: bool=True):
    """Displays a command-line interface to the user for viewing and/or modifying current settings.

    Parameters
    ----------
    ARG_show_header : bool, defaults to 'True'
        If 'True', this function will display this header: 
        "---------- Settings ----------"
    """
    print ()
    if ARG_show_header:
        print (10 * "-", "Settings", 10 * "-")
    global SETTINGS_FILE
    settings = open(SETTINGS_FILE)
    config = configparser.ConfigParser()
    config.read_file(settings)

    settings_sections: list = config.sections()
    if not settings_sections:  # Empty lists/sequences evaluate to False in Python, and this is the PEP8-recommended way to check if a sequence is empty.
        print (textwrap.fill ("WARNING: The setting file appears to be blank. Please close Rosevomit and restart it - Rosevomit should detect a corrupted settings file and offer to restore the settings file to its default state."))
        input ()
        return
    print ("The current settings are listed below in the format")
    print ("  'SECTION'")
    print ("    'OPTION': 'VALUE'")
    print ()
    for section in settings_sections:
        print ()
        print (f"  {section}")
        options = config.items (section)
        if not options:
            print (f"    (no options in this section)")
        else:
            for item in options:
                key = item[0]
                value = item[1]
                print (f"    {key}: {value}")
    print ()

    do_we_change_settings: bool = prompt_to_change_settings()
    assert isinstance (do_we_change_settings, bool)
    if do_we_change_settings is True:
        dialog_change_setting ()
        settings_user_interface (ARG_show_header=False)
    else:
        return  # return to whatever menu/function called this function
