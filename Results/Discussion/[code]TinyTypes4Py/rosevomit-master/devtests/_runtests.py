# This Python file uses the following encoding: utf-8
"""This file contains the main test script for Rosevomit. Running this script will prompt you to choose which tests to run, and then will capture the output of those tests in text files created in this directory."""
import os
import pathlib
import platform
import statistics
import sys
import textwrap
import time
import traceback

# Rosevomit test modules
import cli
import formatting
import messages
import tests
import testutilities
from constants import ALL_TESTS, DATESTRING, DATESTRING_SHORT, FINDIMPORTS_AVAILABLE, PROJECT_NAME, PYLINT_AVAILABLE

from context import rosevomit

if __name__ != "__main__":
    print (textwrap.fill ("YOU ARE TRYING TO RUN 'RunTests.py' AS A MODULE, AND YOU DIDN'T PROGRAM THIS FILE TO RUN THAT WAY! IT MAY NOT WORK PROPERLY. IF YOU MEANT TO DO THIS, THEN GO TO 'RunTests.py' AND REMOVE THIS WARNING AFTER YOU'VE LOOKED THE FILE OVER TO MAKE SURE IT WON'T START CREATING FILES IN STRANGE PLACES, ETC."))
    input()
    sys.exit(1)

# ---------------------MAIN PROGRAM BEGINS---------------------
STARTING_DIRECTORY = pathlib.Path.cwd()
# The program begins by asking the user to determine which tests should be run.
available_tests = [
    "sanity",
    "performance",
    ]
if FINDIMPORTS_AVAILABLE is True:
    available_tests.append ("imports")
    available_tests.append ("unused imports")
if PYLINT_AVAILABLE is True:
    available_tests.append ("pylint")
tests_to_run: list = cli.choose_prompt (available_tests)
num_tests_to_run = len (tests_to_run)
assert num_tests_to_run >= 0
if num_tests_to_run == 0:
    print ("No tests selected. Exiting now.")
    sys.exit()

# Make sure our working directory is the /devtest directory (which this file should be in)
os.chdir (STARTING_DIRECTORY)
if STARTING_DIRECTORY.name != "devtests":
    try:
        os.chdir("devtests")
    except FileNotFoundError as e:  # 'FileNotFoundError' works on directories, too
        print(e)
        traceback.format_exc()
        input ("Press enter to quit.")
        sys.exit(1)

# Creating a 'testlog' directory (TESTLOG_DIR) where we'll store the test results
testlogname = str(DATESTRING_SHORT + "-test")
testlogname = testutilities.make_name_unique (testlogname)
os.mkdir (testlogname)
os.chdir (testlogname)
TESTLOG_DIR = pathlib.Path.cwd()

# Moving through filesystem, looking for important directories and saving their paths as constants. Note that, as written, this program basically just looks for the directories in their expected location and freaks out if they're not there.
os.chdir ("..")
if testutilities.get_cwd_name_only() == "devtests":  # NOTE: We use '==' here, not 'is'!
    DEVTEST_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
os.chdir ("..")
if testutilities.get_cwd_name_only() == "rosevomitrepo":
    REPO_DIR = pathlib.Path.cwd()
else:
    raise FileNotFoundError
# From here, we check the main rosevomit sub-modules all together.
ROSEVOMIT_DIR = REPO_DIR / "rosevomit"
CLI_DIR = ROSEVOMIT_DIR / "programcli"
LOGIC_DIR = ROSEVOMIT_DIR / "programlogic"
DATA_DIR = ROSEVOMIT_DIR / "programdata"
TEMP_DIR = ROSEVOMIT_DIR / "temp"
directories = [ROSEVOMIT_DIR, CLI_DIR, LOGIC_DIR, DATA_DIR, TEMP_DIR]
directories_present = []
directories_missing = []
for item in directories:
    try:
        assert pathlib.Path.exists(item)
        directories_present.append(item)
    except AssertionError:
        directories_missing.append(item)

# ---------------------TESTING BEGINS---------------------
successful_tests = []
failed_tests = []
t0 = time.perf_counter()
print ()
# Running sanity test, performance test, and saving output to file
if "sanity" in tests_to_run:
    print ("Running sanity tests... ", end="")
    sanity_finish: bool = tests.sanity (ARG_test_directory=TESTLOG_DIR)
    assert isinstance (sanity_finish, bool)
    if sanity_finish is True:
        successful_tests.append ("sanity")
        print ("done.")
    else:
        failed_tests.append ("sanity")
        print ("error.")

# Running performance tests...
if "performance" in tests_to_run:
    print ("Running performance tests... ", end="")
    perftest10_results, perftest100_results, perftest1000_results = tests.performance (ARG_test_directory=TESTLOG_DIR)
    successful_tests.append ("performance")
    print ("done.")
else:
    perftest10_results = {}
    perftest100_results = {}
    perftest1000_results = {}

# Generating imports list...
if "imports" in tests_to_run:
    print ("Generating import list... ", end="")
    imports_finish: bool = tests.imports (ARG_test_directory=TESTLOG_DIR, ARG_rosevomit_directory=ROSEVOMIT_DIR)
    assert isinstance (imports_finish, bool)
    if imports_finish is True:
        successful_tests.append ("imports")
        print ("done.")
    else:
        failed_tests.append ("imports")
        print ("error.")

# Generating unused imports list...
if "unused imports" in tests_to_run:
    print ("Generating unused import list... ", end="")
    unusedimports_finish: bool = tests.unused_imports (ARG_test_directory=TESTLOG_DIR, ARG_rosevomit_directory=ROSEVOMIT_DIR)
    assert isinstance (unusedimports_finish, bool)
    if unusedimports_finish is True:
        successful_tests.append ("unused imports")
        print ("done.")
    else:
        failed_tests.append ("unused imports")
        print ("error.")

# Running pylint tests...
if "pylint" in tests_to_run:
    print ("Running pylint... ", end="")
    pylint_finish: bool = tests.pylint (ARG_test_directory=TESTLOG_DIR, ARG_repository_directory=REPO_DIR)
    assert isinstance (pylint_finish, bool)
    if pylint_finish is True:
        successful_tests.append ("pylint")
        print ("done.")
    else:
        failed_tests.append ("pylint")
        print ("error.")

t1 = time.perf_counter()
time_elapsed = t1 - t0


# ---------------------SUMMARY FILE BEGINS---------------------
os.chdir (TESTLOG_DIR)
print ("Writing summary file... ", end="")
with open(DATESTRING_SHORT + ".summary.txt", "w+") as f:
    # Save original stdout and stderr settings
    _old_stdout = sys.stdout
    _old_stderr = sys.stderr
    # Switch stdout and stderr to file output
    sys.stdout = f
    sys.stderr = f

    # HEADER
    print (PROJECT_NAME, "test suite results")
    print (DATESTRING)

    # ENVIRONMENT SUMMARY
    formatting.line ()
    formatting.header ("ENVIRONMENT")
    print ("Python version:", platform.python_version(), platform.python_implementation())
    pybuild = platform.python_build()
    print ("  build:", pybuild[0])
    print ("        ", pybuild[1])
    print ("  compiler:", platform.python_compiler())
    print ("Python path:")
    for p in sys.path:
        print ("  ", p)

    # TEST AND PROGRAM OVERVIEW
    formatting.line ()
    formatting.header ("TEST AND PROGRAM OVERVIEW")
    MAJOR_VERSION = rosevomit.core.constants.MAJOR_VERSION
    MINOR_VERSION = rosevomit.core.constants.MINOR_VERSION
    PATCH_VERSION = rosevomit.core.constants.PATCH_VERSION
    IS_DEVBUILD = rosevomit.core.constants.IS_DEVBUILD
    print (f"Rosevomit version: {MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}")
    if IS_DEVBUILD is True:
        print ("  --!! DEVBUILD !!--")
    print ()
    print ("Directories found:", len (directories_present))
    for item in directories_present:
        print ("  ", item)
    print ()
    print ("Directories not found:", len (directories_missing))
    for item in directories_missing:
        print ("  ", item)
    print ()

    if FINDIMPORTS_AVAILABLE is False:
        print (textwrap.fill ("The third-party module 'findimports' was not present, therefore the following tests were not run: import list, unused imports list"))

    num_successful_tests = len (successful_tests)
    print (f"Tests successfully run: {num_successful_tests}")
    if num_successful_tests > 0:
        print (textwrap.fill (f"  {successful_tests}"))
    num_failed_tests = len (failed_tests)
    print (f"Tests failed to run: {num_failed_tests}")
    if num_failed_tests > 0:
        print (textwrap.fill (f"  {failed_tests}"))
    display_testtime = round (time_elapsed, ndigits=1)
    if display_testtime >= 60:
        # For explanations of the '//' and '%' operators, see here: https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
        display_minutes = int (time_elapsed // 60)
        display_seconds = round ((time_elapsed % 60), ndigits=1)
        print (f"Time to run tests: {display_testtime} seconds ({display_minutes} minutes, {display_seconds} seconds)")
    else:  # If the tests took less than a minute, we don't need to show the conversion from seconds to minutes
        print (f"Time to run tests: {display_testtime} seconds")
    print ()
    num_all_tests = len (ALL_TESTS)
    print (f"All tests: {num_all_tests}")
    if num_all_tests > 0:
        print (textwrap.fill (f"  {ALL_TESTS}"))
    num_available_tests = len (available_tests)
    print (f"Available tests: {num_available_tests}")
    if num_available_tests > 0:
        print (textwrap.fill (f"  {available_tests}"))
    print (f"Tests selected to run: {num_tests_to_run}")
    if num_tests_to_run > 0:
        print (textwrap.fill (f"  {tests_to_run}"))

    # SANITY TEST SUMMARY
    if "sanity" in tests_to_run:
        formatting.line ()
        formatting.header ("GENERATOR SANITY TEST")
    if "sanity" in failed_tests:
        messages.test_no_finish_message ("sanity")
    if "sanity" in successful_tests:
        messages.test_finish_message ("sanity")

    # PERFORMANCE TEST SUMMARY
    if "performance" in tests_to_run:
        formatting.line ()
        formatting.header ("PERFORMANCE TEST")
    if "performance" in failed_tests:
        messages.test_no_finish_message ("performance")
    if "performance" in successful_tests:
        # TODO: See below
        print (textwrap.fill ("TODO: Need to distinguish between minimum, minimum average, and real average. Or, need to find a better naming scheme."))
        print ()
        print ("Fastest performance when generating 10 names, per namelist:")
        for key, value in perftest10_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 10), ndigits=2)
            display_avg = round ((meanresult / 10), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")
        print ()
        print ("Fastest performance when generating 100 names, per namelist:")
        for key, value in perftest100_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 100), ndigits=2)
            display_avg = round ((meanresult / 100), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")
        print ()
        print ("Fastest performance when generating 1,000 names, per namelist:")
        for key, value in perftest1000_results.items():
            # Also converts results from seconds to milliseconds for readibility
            minresult = min (value) * 1000
            maxresult = max (value) * 1000
            meanresult = statistics.mean (value) * 1000
            display_min = int (round (minresult, ndigits=0))
            display_min_avg = round ((minresult / 1000), ndigits=2)
            display_avg = round ((meanresult / 1000), ndigits=2)
            print (f"   {key}: {display_min}ms total, avg {display_min_avg}ms per name. (Real avg {display_avg}ms)")

    # IMPORT SUMMARY
    if "imports" in tests_to_run:
        formatting.line ()
        formatting.header ("IMPORTS")
    if "imports" in failed_tests:
        messages.test_no_finish_message ("imports")
    if "imports" in successful_tests:
        messages.test_finish_message ("imports")

    # UNUSED IMPORT SUMMARY
    if "unused imports" in tests_to_run:
        formatting.line ()
        formatting.header ("UNUSED IMPORTS")
    if "unused imports" in failed_tests:
        messages.test_no_finish_message ("unused-imports")
    if "unused imports" in successful_tests:
        messages.test_finish_message ("unused imports")

    # PYLINT TEST SUMMARY
    if "pylint" in tests_to_run:
        formatting.line ()
        formatting.header ("PYLINT TEST")
    if "pylint" in failed_tests:
        messages.test_no_finish_message ("pylint")
    if "pylint" in successful_tests:
        messages.test_finish_message ("pylint")

    # Restore stdout and stderr to original settings
    sys.stderr = _old_stderr
    sys.stdout = _old_stdout
print ("done.")

print ()
print ("Testing complete. One or more text files with the test results have")
print ("been placed in:")
print ("  ", TESTLOG_DIR)
print ()
