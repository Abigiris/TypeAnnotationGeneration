# This Python file uses the following encoding: utf-8
"""This file contains some constants for the devtests module."""
import datetime

try:
    import findimports
except ImportError:
    FINDIMPORTS_AVAILABLE = False
else:
    FINDIMPORTS_AVAILABLE = True

try:
    from pylint import lint as linter
except ImportError:
    PYLINT_AVAILABLE = False
else:
    PYLINT_AVAILABLE = True

# Setting some constants that will be used in report headers, filenames, titles, etc.
PROJECT_NAME = "Rosevomit"
current_time = datetime.datetime.now()
DATESTRING = current_time.strftime ("%Y-%b-%d (%a) %I:%M%p")
DATESTRING_SHORT = current_time.strftime ("%Y%b%d-%H%M")

ALL_TESTS: list = [
    "sanity",
    "performance",
    "imports",
    "unused imports",
    "pylint"
]
