# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# suncal_helpers.py
# rosevomit.programlogic.suncalc_helpers
# ___________________________________________________________________
# pylint: skip-file
"""A file that contains helper functions for the main suncalc function contained in 'suncalc.py'."""
import csv
from decimal import Decimal
from math import asin, atan2
from math import pi
from typing import IO

from core import logs
from core.utilities import Angle, deg2rad, rad2deg, angle_sanity_check

_SUNCALCHELPER = logs.BaseLogger(__name__)

# defaults
AXIAL_TILT = 10  # Note that axial tilt is also called "obliquity of the ecliptic"


def antikythera_rotation_angle (astrodate):
    """Returns the 'Antikythera Rotation Angle', equivalent to Earth's 'Earth Rotation Angle' and similar to Earth's 'Greenwich Sidereal Time', though Earth's GST includes an adjustment for the procession of Earth's March equinox that is irrelevant for Antikythera.

    Parameters
    ----------
    astrodate
        The fractional day of the year.

    Returns
    -------
    rotation_angle
        The rotation angle of the planet, measured in degrees (°).
    """
    # validating
    if 0 <= astrodate <= 365:
        pass
    else:
        raise ValueError
    # calculating current rotation angle
    rotation_angle = astrodate * (360 + Decimal(0.9856))
    rotation_angle = angle_sanity_check (rotation_angle)
    # rotation_angle = rotation_angle
    return rotation_angle


def sun_alt_az (fractionalday, latitude, longitude):
    """Expects latitude and longitude in degrees.
    """
    global AXIAL_TILT
    latitude = Angle(latitude)
    longitude = Angle(longitude)
    ϵ = Angle(f"{AXIAL_TILT}")
    julianday = Decimal(f"{fractionalday}") - Decimal("0.5")

    # first, we need to calculate the position of the sun in the ecliptic coordinate system
        # Mean longitude is the ecliptic longitude that an orbiting body could be found at, if its orbit were circular and free of perturbations. Because our orbit actually *is*, our mean longitude actually *does* equal the ecliptic longitude.
        # In a circular orbit, mean longitude = ecliptic longitude.
        # In a circular orbit with 0 inclination, mean anomaly = mean longitude = ecliptic longitude
    ecliptic_longitude = Angle(julianday * Decimal(f"{360 / 365}"))
    λ = ecliptic_longitude
    ecliptic_latitude = Angle(Decimal('0'))
    β = ecliptic_latitude

    # next, we need to convert the ecliptic coordinates into equitorial coordinates
        # ra and declination
    right_ascension = Decimal(atan2 (ϵ.cos_inradians * λ.sin_inradians, λ.cos_inradians))
    declination = Decimal(asin (ϵ.sin_inradians * λ.sin_inradians))
    right_ascension = Angle(rad2deg(right_ascension))
    declination = Angle(rad2deg(declination))
    α = right_ascension
    δ = declination
        # hour angle
    ara = antikythera_rotation_angle (fractionalday)
    ara = Angle(ara)
    hour_angle = (ara.inradians + Decimal(pi)) + latitude.inradians - α.inradians
    h = Angle(rad2deg(hour_angle))

    # finally, we need to convert the ecliptic coordinates into horizontal coordinates
        # azimuth
    part1 = (-latitude.sin_inradians * δ.cos_inradians * h.cos_inradians) + (latitude.cos_inradians * δ.sin_inradians)
    part2 = δ.cos_inradians * h.sin_inradians
    azimuth = Decimal(-atan2(part1, part2))
        # altitude
    altitude = Decimal(asin ((latitude.sin_inradians * δ.sin_inradians) + (latitude.cos_inradians * δ.cos_inradians * h.cos_inradians)))

    azimuth = rad2deg(azimuth)
    altitude = rad2deg(altitude)
    return (altitude, azimuth)


def finalformatting_degrees (x):
    assert isinstance (x, (int, float, Decimal))
    _result = round(x, 2)
    if _result >= 0:
        _sign = "+"
    else:
        _sign = "-"
    _result = abs(_result)  # to remove sign
    _result = float(_result)  # to ensure decimal
    # splitting up so we can measure section length and pad with appropriate spaces
    _part1, _part2 = str(_result).split(".")
    _extra_spaces = (3 - len(_part1)) * " "
    _extra_zeroes = (2 - len(_part2)) * "0"
    _result = _sign + _extra_spaces + _part1 + "." + _part2 + _extra_zeroes + "°"
    return _result


def getsunrise_and_sunset(x):
    """Given a list of tuples in (timestamp: str, altitude: float) format, returns the timestamps of the local sunrise and sunset.
    """
    local_x = x.copy()
    assert isinstance (local_x, list)
    # Get sunrise
    solar_alt_tuple = local_x.pop(0)
    assert isinstance (solar_alt_tuple, tuple)

    sunrise_string = "No sunrise."
    sunset_string = "No sunset"
    try:
        if solar_alt_tuple[1] > 0:
            sunrise_string = "Sun already up."
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
        elif solar_alt_tuple[1] == 0:
            sunrise_string = solar_alt_tuple[0]
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
        else:
            while solar_alt_tuple[1] < 0:
                solar_alt_tuple = local_x.pop(0)
            sunrise_string = solar_alt_tuple[0]
            while solar_alt_tuple[1] > 0:
                solar_alt_tuple = local_x.pop(0)
            sunset_string = solar_alt_tuple[0]
    except IndexError:
        pass
    finally:
        return sunrise_string, sunset_string


def startfile_csv(ARG_filewriter: IO):
    """Writes the header for the .csv suncalc results file.

    Parameters
    ----------
    ARG_filewriter : IO
        The file writing IO object.
    
    Returns
    -------
    csvwriter : csv._writer
        The IO object formatted specifically for this csv file.
    """
    csvwriter = csv.writer(ARG_filewriter, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
    csvheaders = ["DAY", "HOUR24", "MINUTE", "FRACTIONAL DAY", "DATESTRING", "ALTITUDE", "AZIMUTH"]
    csvwriter.writerow (csvheaders)
    return csvwriter


def startfile_txt(ARG_filewriter: IO, ARG_coordinates: tuple):
    """Writes the header for the .txt suncalc results file.

    Parameters
    ----------
    ARG_filewriter : IO
        The file writing IO object.
    ARG_coordinates : tuple
        A tuple containing (latitude, longitude)
    """
    lat, long = ARG_coordinates
    ARG_filewriter.write (f"LATITUDE: {lat} LONGITUDE: {long} \n")
    ARG_filewriter.write (f"{44 * '-'} \n")


def get_12hr_time (ARG_hour24: int):
    """Converts time from a 24-hour format to a 12-hour format.

    Parameters
    ----------
    ARG_hour24 : int
        The hour of the day according to a 24-hour clock.

    Returns
    -------
    H12 : int
        The hour of the day according to a 12-hour clock.
    period : str
        Either "am" or "pm"
    """
    H24 = ARG_hour24
    if H24 < 12:
        period = "am"
        H12 = H24
    elif H24 == 12:
        period = "pm"
        H12 = H24
    else:
        period = "pm"
        H12 = H24 - 12
    return H12, period
