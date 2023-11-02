# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# citycoordinates.py
# rosevomit.programdata.citycoordinates
# ___________________________________________________________________
"""A data file containing the coordinates (latitude and longitude) of various cities and locations throughout Antikythera."""
from core import logs

_CITYCOORDINATES_LOGGER = logs.BaseLogger (__name__)

PLACES = {
    "City2": (0, 40),
    "Cordu": (-75, -70),
}
