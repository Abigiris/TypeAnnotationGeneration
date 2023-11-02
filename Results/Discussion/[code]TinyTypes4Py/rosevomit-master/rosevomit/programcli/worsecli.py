# worsecli.py
# rosevomit.programcli.worsecli
# ___________________________________________________________________
"""A UI module that contains functions for displaying menus beyond Rosevomits's main menu, and for processing the inputs for those menus.

WILL BE REPLACED EVENTUALLY BY rosevomit.programcli.bettercli
"""
import re

from programcli import messages
from core import logs, settings
from programlogic import logiccontroller, exiting

_WORSECLI_LOGGER = logs.BaseLogger (__name__)


def input_integer(ARG_prompt_text: str="", ARG_if_invalid=None):
    """Prompts the user for an integer, and checks to make sure that the user's input is actually an integer. If it is, it returns the integer. If it is not, it informs the user of the invalid input and prompts them again for valid input or runs the function passed to it through the 'ARG_if_invalid' argument."""
    _prompt = ARG_prompt_text.strip()
    if _prompt == "" or _prompt is None:
        _input = input ("Please enter a positive integer: ")
    else:
        _input = input (f"{_prompt} ")
    _input = _input.strip()
    try:
        _input = abs (int (_input))
        return _input
    except ValueError:
        print ("Sorry, that's not a valid number.")
        if ARG_if_invalid == "" or ARG_if_invalid is None:
            recursive_result = input_integer(_prompt)
            return recursive_result
        else:
            result = ARG_if_invalid()
            return result


def submenu_about_show():
    """Contains the display instructions for the about menu. Accepts no parameters, returns nothing."""
    print ()
    print ("What information do you wish to display?")
    print ("    1. About Rosevomit")
    print ("    2. Licensing information")
    print ("    0. Back to main menu.")
    print ()


def submenu_about_input():
    """Asks for user input and processes it. Contains logic for the about submenu."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.strip()  # Strips whitespaces

    if menuchoice == "1":
        messages.about_program_message()
    elif menuchoice == "2":
        messages.about_license_message()
    elif menuchoice == '0':
        pass
    elif menuchoice in ("help", "HELP", "'help'", "h", "H", "helf", "HELF"):
        submenu_about_show()
        submenu_about_input()
    elif menuchoice == "":
        submenu_about_input()
    else:
        messages.unrecognized_input_message (menuchoice)
        submenu_about_input()


def submenu_name_show():
    """Contains display instructions for the name generation menu. Accepts no parameters, returns nothing."""
    print ()
    print ("What sorts of names would you like to generate?")
    print ("     1. First names")
    print ("     2. First names, female-only")
    print ("     3. First names, male-only")
    print ("     4. Last names")
    print ("     5. Full names")
    print ("     6. Full names, female-only")
    print ("     7. Full names, male-only")
    print ("     0. Back to main menu.")
    print ()


def submenu_name_input():
    """Asks for user input and processes it. Contains logic for the name generation submenu. Accepts no parameters, returns nothing."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.strip()  # Strips whitespaces

    if menuchoice == "1":
        _input = input_integer ("How many first names should be generated? ")
        print ()
        logiccontroller.generate_names("first", int(_input))
        print ()
    elif menuchoice == "2":
        _input = input_integer ("How many female first names should be generated? ")
        print ()
        logiccontroller.generate_names("firstfemale", int(_input))
        print ()
    elif menuchoice == "3":
        _input = input_integer ("How many male first names should be generated? ")
        print ()
        logiccontroller.generate_names("firstmale", int(_input))
        print ()
    elif menuchoice == "4":
        _input = input_integer ("How many last names should be generated? ")
        print ()
        logiccontroller.generate_names("last", int(_input))
        print ()
    elif menuchoice == "5":
        _input = input_integer ("How many full names should be generated? ")
        print ()
        logiccontroller.generate_names("full", int(_input))
        print ()
    elif menuchoice == "6":
        _input = input_integer ("How many female full names should be generated? ")
        print ()
        logiccontroller.generate_names("fullfemale", int(_input))
        print ()
    elif menuchoice == "7":
        _input = input_integer ("How many male full names should be generated? ")
        print ()
        logiccontroller.generate_names("fullmale", int(_input))
        print ()
    elif menuchoice == '0':
        pass
    elif menuchoice in ("help", "HELP", "'help'", "h", "H", "helf", "HELF"):
        submenu_name_show()
        submenu_name_input()
    elif menuchoice == "":
        submenu_name_input()
    else:
        messages.unrecognized_input_message (menuchoice)
        submenu_name_input()


def submenu_timeline_show():
    """Contains display instructions for the timeline generation menu. Accepts no parameters, returns nothing."""
    print ()
    print ("What sort of timeline would you like to generate?")
    print ("     1. Global events")
    print ("     2. Regional events (NOT CURRENTLY SUPPORTED)")
    print ("     0. Back to main menu.")
    print ()


def submenu_timeline_input():
    """Asks for user input and processes it. Contains logic for the name generation submenu. Accepts no parameters, returns nothing."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.strip()  # Strip whitespaces

    if menuchoice == "1":
        _input = input_integer ("How many years of historical global events should be generated? ")
        print ()
        logiccontroller.gen_timeline("globalevents", int(_input))
        print ()
    elif menuchoice == "2":
        print ("This option is not currently supported.")
        submenu_timeline_input ()
    elif menuchoice == '0':
        pass
    elif menuchoice in ("help", "HELP", "'help'", "h", "H", "helf", "HELF"):
        submenu_timeline_show()
        submenu_timeline_input()
    elif menuchoice == "":
        submenu_timeline_input()
    else:
        messages.unrecognized_input_message (menuchoice)
        submenu_timeline_input()


def submenu_suncalc_show():
    """Displays user options for Suncalc. Accepts no parameters, returns nothing."""
    print ()
    print ("What are the observer's coordinates?")
    print ("     1. Default (0, 0)")
    print ("     2. Pick a preset place (NOT CURRENTLY SUPPORTED)")
    print ("     3. I'll enter the coordinates myself, goddammit!")
    print ()


def submenu_suncalc_input():
    """Asks for user input for Suncalc."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.strip()  # Strips whitespaces

    if menuchoice == "1":
        lat = 0
        long = 0
        return lat, long
    elif menuchoice == "2":
        print ("This option is not currently supported.")
        recursive_result = submenu_suncalc_input ()
        return recursive_result
    elif menuchoice == '3':
        lat = input ("Enter latitude: ")
        long = input ("Enter longitude: ")
        lat = float(lat)
        long = float(long)
        return lat, long
    elif menuchoice in ("help", "HELP", "'help'", "h", "H", "helf", "HELF"):
        submenu_suncalc_show()
        recursive_result = submenu_suncalc_input()
        return recursive_result
    elif menuchoice == "":
        recursive_result = submenu_suncalc_input()
        return recursive_result
    else:
        messages.unrecognized_input_message (menuchoice)
        recursive_result = submenu_suncalc_input()
        return recursive_result


def prompt_save() -> bool:
    """Asks the user if they want to save, and processes response."""
    menuchoice = input ("Would you like to save this result? (Yes/No) ")
    menuchoice = menuchoice.strip()  # Strips whitespaces

    if re.search(r"^[y][es]*$", menuchoice, flags=re.IGNORECASE):
        return True
    elif re.search(r"^[n][o]*$", menuchoice, flags=re.IGNORECASE):
        return False
    else:
        messages.unrecognized_input_message (menuchoice)
        recursive_result = prompt_save()
        return recursive_result


def show_main_menu():
    """Contains display instructions for the main menu. Accepts no parameters, returns nothing."""
    print ()
    print (10 * "-", "Rosevomit.py Main Menu", 10 * "-")
    print ("What would you like do?")
    print ("     1. Generate random names")
    print ("     2. Generate a random timeline")
    print ("     3. Calculate the sun's position (EXPERIMENTAL)")
    print ("     8. Program information")
    print ("S or 9. Program settings")
    print ("X or 0. Exit program")
    print ()


def ask_for_input():
    """Asks for user input and processes it. Contains logic for the main menu. Accepts no parameters, returns nothing."""
    menuchoice = input ("Enter your choice, or type 'help' for current menu: ")
    menuchoice = menuchoice.rstrip()  # Strips whitespaces at the end.

    if menuchoice == "1":
        submenu_name_show()
        submenu_name_input()
        show_main_menu()
    elif menuchoice == "2":
        submenu_timeline_show()
        submenu_timeline_input()
        show_main_menu()
    elif menuchoice == "3":
        submenu_suncalc_show()
        lat, long = submenu_suncalc_input()
        logiccontroller.gen_suncalc(lat, long)
        show_main_menu()
    elif menuchoice == "8":
        submenu_about_show()
        submenu_about_input()
        show_main_menu()
    elif menuchoice in ("9", "S", "s", "setting", "settings"):
        settings.settings_user_interface (ARG_show_header=True)
        show_main_menu()
    elif menuchoice in ("0", "X", "x", "exit"):
        exiting.exit_rosevomit()
    elif menuchoice in ("help", "HELP", "'help'", "h", "H", "helf", "HELF"):
        show_main_menu()
    elif menuchoice == "":
        ask_for_input()
    else:
        print (f"{menuchoice} is not a recognized command.")
