# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# randomevent.py
# rosevomit.programlogic.randomevent
# ___________________________________________________________________
"""A file that contains functions for randomly generating annual events."""
import os
import random


from core import logs


_RANDOMEVENTLOGGER = logs.BaseLogger (__name__)


def check_volcano(ARG_in_year, ARG_csv_destination=""):
    """Checks to see if a volcano explodes. Returns text to display onscreen, and also possibly writes some data related to each event to the specified file.

    Parameters
    ----------
    ARG_in_year
        "...in this year, something happened..."
    ARG_csv_destination (defaults to "")
        The file to store results in. Should include '.csv' extension.
    """
    # Validating arguments
    if os.path.isfile (f"{ARG_csv_destination}") is True:
        _write_to_file = True
    else:
        _write_to_file = False
    if isinstance (ARG_in_year, int) is False:
        in_year = -1
    else:
        in_year = ARG_in_year

    _list = []
    _int = random.randint(1, 50000)
    if _int == 1:
        _list.append("...a SUPERVOLCANO erupted, rated at an 8 on the Volcanic Explosivity Index. The global impact is substantial, and the regional impact is catastrophic.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, VEI 8 SUPERVOLCANO \n")
    _int = random.randint(1, 750)
    if _int == 1:
        _list.append("...a MAJOR VOLCANO erupted, rated at an 7 on the Volcanic Explosivity Index and equivalent to the 1815 eruption of Tambora. The global impact is impossible to miss, the regional impact is substantial, and the local impact is catastrophic.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, VEI 7 MAJOR VOLCANO \n")
    _int = random.randint(1, 75)
    if _int == 1:
        _list.append("...a MAJOR VOLCANO erupted, rated at an 6 on the Volcanic Explosivity Index and equivalent to the 1883 eruption of Krakatoa. The global impact is notable, the regional impact is substantial, and the local impact is catastrophic.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, VEI 6 MAJOR VOLCANO \n")
    return _list


def check_earthquake(ARG_in_year, ARG_csv_destination=""):
    """Checks to see if an earthquake occurs. Note that the frequency values here are not exactly based off real-life values. Also note that there are 10 - 20 serious earthquakes (rated X) each year that fall below XI and XII. These are omitted due to their frequency.

    Parameters
    ----------
    ARG_in_year
        "...in this year, something happened..."
    ARG_csv_destination (defaults to "")
        The file to store results in. Should include '.csv' extension.
    """
    # Validating arguments
    if os.path.isfile (f"{ARG_csv_destination}") is True:
        _write_to_file = True
    else:
        _write_to_file = False
    if isinstance (ARG_in_year, int) is False:
        in_year = -1
    else:
        in_year = ARG_in_year

    _list = []
    _int = random.randint(1, 400)
    if _int == 1:
        _list.append("...a CATASTROPHIC EARTHQUAKE occured, rated at an XII on the Modified Mercalli Scale. Very few structures remain standing. All building foundations have been irrepairably damaged. Bridges destroyed. Underground infrastructure and structures destroyed. Waves seen on ground surfaces. Lines of sight and level permanently distorted. Damage total.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, MMS XII CATASTROPHIC EARTHQUAKE \n")
    _int = random.randint(1, 50)
    if _int == 1:
        _list.append("...a MAJOR EARTHQUAKE occured, rated at an XI on the Modified Mercalli Scale. Few masonry structures survive - if any. Some well-built wooden structures survive, though none are unscathed. All building foundations have been severely damaged.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, MMS XI MAJOR EARTHQUAKE \n")
    return _list


def check_impact(ARG_in_year, ARG_csv_destination=""):
    """Checks to see if a asteroid impact occurs. Returns text to display onscreen, and also possibly writes some data related to each event to the specified file.

    Parameters
    ----------
    ARG_in_year
        "...in this year, something happened..."
    ARG_csv_destination (defaults to "")
        The file to store results in. Should include '.csv' extension.
    """
    # Validating arguments
    if os.path.isfile (f"{ARG_csv_destination}") is True:
        _write_to_file = True
    else:
        _write_to_file = False
    if isinstance (ARG_in_year, int) is False:
        in_year = -1
    else:
        in_year = ARG_in_year

    _list = []
    _int = random.randint(1, 440000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 1km wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 1000m (1km) diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 190000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 700m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 700m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 100000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 400m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 400m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 73000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 300m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 300m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 59000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 250m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 250m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 36000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 200m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 200m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 16000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 150m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 150m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 11000)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 130m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 130m diameter ASTEROID IMPACT \n")

    _int = random.randint(1, 5200)
    if _int == 1:
        _list.append("...an ASTEROID IMPACT occured. It was 100m wide.")
        if _write_to_file is True:
            (open (ARG_csv_destination, "a+")).write (f"{in_year}, 100m diameter ASTEROID IMPACT \n")

    return _list


def check_astronomy(ARG_in_year, ARG_csv_destination=""):
    """Checks to see if a supernova becomes visible. Returns text to display onscreen, and also possibly writes some data related to each event to the specified file.

    Parameters
    ----------
    ARG_in_year
        "...in this year, something happened..."
    ARG_csv_destination (defaults to "")
        The file to store results in. Should include '.csv' extension.
    """
    # Validating arguments
    if os.path.isfile (f"{ARG_csv_destination}") is True:
        _write_to_file = True
    else:
        _write_to_file = False
    if isinstance (ARG_in_year, int) is False:
        in_year = -1
    else:
        in_year = ARG_in_year

    _list = []
    _int = random.randint(1, 300)
    if _int == 1:
        _int = random.randint(1, 4)
        if _int == 1:
            _list.append("...a star suddenly brightened, becoming a SUPERNOVA. It remains visible for many months.")
            if _write_to_file is True:
                (open (ARG_csv_destination, "a+")).write (f"{in_year}, A STAR BRIGHTENS SUDDENLY - A SUPERNOVA! \n")
        else:
            _list.append("...a new star, a SUPERNOVA, became visible. It remains visible for many months.")
            if _write_to_file is True:
                (open (ARG_csv_destination, "a+")).write (f"{in_year}, A NEW STAR APPEARS SUDDENLY- A SUPERNOVA! \n")
    return _list
