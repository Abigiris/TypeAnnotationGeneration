# This Python file uses the following encoding: utf-8
"""This file contains the functions for the main tests for Rosevomit. These tests should all be called by the script in '_runtests.py'."""
import os
import sys
import unittest

try:
    import findimports
except ImportError:
    FINDIMPORTS_MODULE_EXISTS = False
else:
    FINDIMPORTS_MODULE_EXISTS = True

try:
    from pylint import lint as linter
except ImportError:
    PYLINT_MODULE_EXISTS = False
else:
    PYLINT_MODULE_EXISTS = True

# Rosevomit test modules
from constants import DATESTRING, DATESTRING_SHORT, PROJECT_NAME
import formatting
import messages
_start_directory = os.getcwd()  # pylint: disable=invalid-name
from performancetests import timetest_name_generation  # pylint: disable=wrong-import-position
import sanitytests  # pylint: disable=wrong-import-position
import testutilities  # pylint: disable=wrong-import-position
# Rosevomit itself
from context import rosevomit  # pylint: disable=wrong-import-position
os.chdir (_start_directory)

# --------------------- SANITY TEST ---------------------
def sanity(ARG_test_directory):
    """Runs the sanity test"""
    os.chdir (ARG_test_directory)
    with open(DATESTRING_SHORT + ".sanity.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        formatting.line ()
        formatting.header ("GENERATOR SANITY TEST")
        print ()

        try:
            testsuite = unittest.TestLoader().loadTestsFromModule(sanitytests)
            unittest.TextTestRunner(verbosity=2).run(testsuite)
        except Exception:  # pylint: disable=broad-except
            messages.traceback_message()
            did_test_finish = False
        else:
            did_test_finish = True

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    return did_test_finish


# --------------------- PERFORMANCE TEST ---------------------
def performance(ARG_test_directory):
    """Runs the performance test"""
    os.chdir (ARG_test_directory)
    with open(DATESTRING_SHORT + ".perf.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        formatting.line ()
        formatting.header ("PERFORMANCE TEST FULL RESULTS")
        print ()

        try:
            print ("Rosevomit's performance when generating 10 names (measured in seconds)")
            with testutilities.Suppressor():
                perftest10_results = timetest_name_generation (ARG_number_of_names=10)
            for key, value in perftest10_results.items():
                print (f"   {key}: {value}")
            print ()
            print ("Rosevomit's performance when generating 100 names (measured in seconds)")
            with testutilities.Suppressor():
                perftest100_results = timetest_name_generation (ARG_number_of_names=100)
            for key, value in perftest100_results.items():
                print (f"   {key}: {value}")
            print ()
            print ("Rosevomit's performance when generating 1,000 names (measured in seconds)")
            with testutilities.Suppressor():
                perftest1000_results = timetest_name_generation (ARG_number_of_names=1000)
            for key, value in perftest1000_results.items():
                print (f"   {key}: {value}")
        except Exception:  # pylint: disable=broad-except
            messages.traceback_message()

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    return perftest10_results, perftest100_results, perftest1000_results


# --------------------- IMPORTS TEST ---------------------
def imports(ARG_test_directory, ARG_rosevomit_directory):
    """Runs the import list test."""
    os.chdir (ARG_test_directory)
    with open(DATESTRING_SHORT + ".imports.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        formatting.line ()
        formatting.header ("full imports list")
        os.chdir (ARG_rosevomit_directory)
        mock_cli_args = ["rosevomit.py", "-i"]

        try:
            findimports.main(argv=mock_cli_args)
        except Exception:  # pylint: disable=broad-except
            messages.traceback_message()
            did_test_finish = False
        else:
            did_test_finish = True

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    return did_test_finish


# --------------------- UNUSED IMPORTS TEST ---------------------
def unused_imports(ARG_test_directory, ARG_rosevomit_directory):
    """Runs the unused import list test."""
    os.chdir (ARG_test_directory)
    with open(DATESTRING_SHORT + ".imports-unused.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        formatting.line ()
        formatting.header ("UNUSED IMPORTS LIST")
        os.chdir (ARG_rosevomit_directory)
        mock_cli_args = ["rosevomit.py", "-i", "-u"]

        try:
            findimports.main(argv=mock_cli_args)
        except Exception:  # pylint: disable=broad-except
            messages.traceback_message()
            did_test_finish = False
        else:
            did_test_finish = True

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    return did_test_finish


# --------------------- PYTLINT TEST ---------------------
def pylint(ARG_test_directory, ARG_repository_directory):
    """Runs a test using pylint"""
    os.chdir (ARG_test_directory)
    with open(DATESTRING_SHORT + ".pylint.txt", "w+") as f:
        # Save original stdout and stderr settings
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        # Switch stdout and stderr to file output
        sys.stdout = f
        sys.stderr = f

        print (PROJECT_NAME, "test suite results")
        print (DATESTRING)
        formatting.line ()
        formatting.header ("pylint")
        os.chdir (ARG_repository_directory)
        # pylint error messages
        #   C0301 line-too-long
        #   C0326 spaces
        #   R1705 no-else-return
        #   E0401 import-error (because they don't seem to work properly for me when running statically)
        pylint_opts = [
            "rosevomit",
            "--rcfile=.pylintrc",
            ]

        try:
            linter.Run (pylint_opts, do_exit=False)
        except Exception:  # pylint: disable=broad-except
            messages.traceback_message()
            did_test_finish = False
        else:
            did_test_finish = True

        # Restore stdout and stderr to original settings
        sys.stderr = _old_stderr
        sys.stdout = _old_stdout
    return did_test_finish
