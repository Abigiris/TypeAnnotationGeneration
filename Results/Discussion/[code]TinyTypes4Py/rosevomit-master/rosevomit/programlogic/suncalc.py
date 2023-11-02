# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# suncalc.py
# rosevomit.programlogic.suncalc
# ___________________________________________________________________
"""A file that contains functions for calculating the position across Antikythera, dependinging on the time and date."""
from decimal import Decimal
import operator
import os
import time

from core import logs
from core.constants import SAVE_DIRECTORY_PATH
from programlogic import antikythera_time, suncalc_helpers

_SUNCALCLOGGER = logs.BaseLogger (__name__)


def main(ARG_lat, ARG_long, ARG_output_file="results"):
    """The main suncalc function.
    Parameters
    ----------
    lat, long
        The observer's coordinates, measured in degrees (°).
    ARG_output_directory (default is None)
        The default directoryto save results in.
    ARG_output_file (default is "results")
        The default name (minus the extension) to be used when naming the save file.
    """
    lat = Decimal(ARG_lat)
    long = Decimal(ARG_long)
    coordinates = (lat, long)
    minute_intervals = [0, 15, 30, 45]
    timed_results = []
    os.chdir (SAVE_DIRECTORY_PATH)
    with open(f"{ARG_output_file}.txt", mode="w+") as textfile, open(f"{ARG_output_file}.csv", mode="w+") as csvfile:
        suncalc_helpers.startfile_txt (textfile, coordinates)
        csvwriter = suncalc_helpers.startfile_csv (csvfile)
        for item in range (1, 366):
            D = item
            textfile.write (f"{15* ' '} AZIMUTH   ALTITUDE  FRACTIONAL DAY\n")
            daily_solar_altitudes = []
            for item in range (0, 24):
                H24 = item
                H12, a = suncalc_helpers.get_12hr_time (H24)
                for item in minute_intervals:
                    M = item
                    fractday = antikythera_time.time2fractday (D, H24, M)
                    starttime = time.time()
                    (alt, az) = suncalc_helpers.sun_alt_az (fractday, lat, long)
                    endtime = time.time()
                    elapsedtime = endtime - starttime
                    timed_results.append (elapsedtime)

                    # text file writing
                    pretty_az = suncalc_helpers.finalformatting_degrees (az)
                    pretty_alt = suncalc_helpers.finalformatting_degrees (alt)
                    HH = str(H12).zfill(2)
                    MM = str(M).zfill(2)
                    timestamp = (f"{HH}:{MM}{a}")
                    datestring = str((f"Day {D}, {timestamp}"))
                    textfile.write (f"{datestring}  {pretty_az}  {pretty_alt}  {fractday}\n")

                    # quick aside to keep track of local altitudes by timestamps
                    daily_solar_altitudes.append ((timestamp, alt))

                    # csv file writing
                    results = [D, H24, M, fractday, datestring, alt, az]
                    csvwriter.writerow (results)

                    # After looping through the minute intervals...
                # ..and looping through the hours...
            # ...we return to look at the results of the day (the "daily_solar_altitudes" list) and extract some information on the sunrises and sunsets and local solar moments from that list.
            local_sunrise, local_sunset = suncalc_helpers.getsunrise_and_sunset (daily_solar_altitudes)
            local_noon = max (daily_solar_altitudes, key=operator.itemgetter(1))[0]
            local_midnight = min (daily_solar_altitudes, key=operator.itemgetter(1))[0]
            local_results_string1 = str(f"Local sunrise: {local_sunrise}  Local sunset: {local_sunset} \n")
            local_results_string2 = str(f"Local noon: {local_noon}  Local midnight: {local_midnight} \n")

            # Then, we write that information to the text file.
            textfile.write (local_results_string1)
            textfile.write (local_results_string2)
            textfile.write ("\n")
            if D == 1:
                print (f"Done with day {D}, ", end="")
            elif 1 < D < 365:
                print (f"{D}, ", end="")
            else:
                print (f"{D}. ", end="")
                avgtime = sum (timed_results) / len (timed_results)
                print (f"Average time per minute interval: {avgtime} seconds")
