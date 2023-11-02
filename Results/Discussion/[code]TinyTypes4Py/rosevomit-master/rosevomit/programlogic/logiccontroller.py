# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# logiccontroller.py
# rosevomit.programlogic.logiccontroller
# ___________________________________________________________________
"""This is the main "logic" file. Its job is to keep track of the program's custom logic modules and to serve as an intermediary in between them and the main file (rosevomit.py). This isn't actually necessary, but it serves as good coding practice for me. Hopefully."""
import datetime
import os
import textwrap

try:
    from core import logs, customerrors, constants
    import core.utilities as ut
    from programcli import dialogsave
    from programlogic import suncalc, randomevent, randomname
except ImportError:
    from rosevomit.core import logs, customerrors, constants
    import rosevomit.core.utilities as ut
    from rosevomit.programcli import dialogsave
    from rosevomit.programlogic import suncalc, randomevent, randomname


_LOGICLOGGER = logs.BaseLogger (__name__)


def generate_names (ARG_nametype: str, ARG_number: int):
    """This function generates a number of random names.

    Parameters
    ----------
    ARG_nametype : str
        Valid nametypes are 'first', 'firstfemale', 'firstmale', 'last', 'full', 'fullfemale', 'fullmale'.
    ARG_number : int
        The number of names to generate.
    """
    if ARG_nametype == "first":
        ut.repeat (randomname.getname_firstany, ARG_number)
    elif ARG_nametype == "firstfemale":
        ut.repeat (randomname.getname_firstfemale, ARG_number)
    elif ARG_nametype == "firstmale":
        ut.repeat (randomname.getname_firstmale, ARG_number)
    elif ARG_nametype == "last":
        ut.repeat (randomname.getname_lastany, ARG_number)
    elif ARG_nametype == "full":
        ut.repeat (randomname.getname_fullany, ARG_number)
    elif ARG_nametype == "fullfemale":
        ut.repeat (randomname.getname_fullfemale, ARG_number)
    elif ARG_nametype == "fullmale":
        ut.repeat (randomname.getname_fullmale, ARG_number)
    else:
        raise ValueError ("rosevomit.programlogic.logiccontroller.generatenames() encountered an unexpected value for 'ARG_nametype'. The value of ARG_nametype was: {}".format(ARG_nametype))


def gen_timeline(ARG_eventtypes: str, ARG_yearrange: int):
    """This function receives the user input and calls functions accordingly.

    Parameters
    ----------
    ARG_eventtypes : str
        The only valid eventtype at the moment is 'globalevents'.
    ARG_yearrange : int
        The number of years to generate events for.
    """
    if ARG_eventtypes == "globalevents":
        def get_events(ARG_timeline_year, ARG_output_file):
            """This function checks to see what events have happened in a given year. It assumes that the probability of events does not change from year to year."""
            events = []
            print (f"{ARG_timeline_year} years ago, scholars tell us...")
            # Run checks to generate events. The randomevent checks return a list whose elements are the event text of events that occured. We add these elements to the "events" list.
            events.extend (randomevent.check_volcano (ARG_timeline_year, ARG_output_file))
            events.extend (randomevent.check_earthquake (ARG_timeline_year, ARG_output_file))
            events.extend (randomevent.check_impact (ARG_timeline_year, ARG_output_file))
            events.extend (randomevent.check_astronomy (ARG_timeline_year, ARG_output_file))
            for item in range (len (events)):
                print (textwrap.fill (f"    {events[item]}", width=70))
                print ()

        try:
            try:
                os.chdir ("./temp/")
            except FileNotFoundError:
                os.chdir ("..")
                os.chdir ("./temp")
        except FileNotFoundError:  # Maybe it's being run by a testing script?
            os.chdir ("..")
            os.chdir ("./rosevomit/temp/")
        _tempfile_name = ut.setname("timeline")
        _tempfile = open(_tempfile_name, "a+")

        _this_year = ARG_yearrange
        for item in range (0, ARG_yearrange):
            get_events (ARG_timeline_year=_this_year, ARG_output_file=_tempfile_name)
            _this_year = (_this_year - 1)

        _tempfile.write ("Testing.")
        _tempfile.close()
    else:
        raise ValueError ("rosevomit.programlogic.logiccontroller.gen_timeline() encountered an unexpected value for 'ARG_eventtypes'. The value of ARG_eventtypes was: {}".format(ARG_eventtypes))


def gen_suncalc (ARG_lat, ARG_long):
    """Calls the suncalc function

    Parameters
    ----------
    ARG_lat, ARG_long
        The observer's latitude and longitude, which will be passed to suncalc.main()
    """
    os.chdir (constants.SAVE_DIRECTORY_PATH)
    current_time = datetime.datetime.now()
    datestring = current_time.strftime ("%Y%b%d-%H%M")
    filename_for_results = "suncalc_" + datestring
    suncalc.main (ARG_lat, ARG_long, ARG_output_file=filename_for_results)
