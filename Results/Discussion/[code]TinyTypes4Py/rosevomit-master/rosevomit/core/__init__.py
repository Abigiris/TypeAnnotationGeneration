# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# __init__.py
# rosevomit.core.__init__
# ___________________________________________________________________
# pylint: disable=wrong-import-position
"""The `rosevomit/core/` directory (folder) holds the files and scripts that are central to Rosevomit's operation."""
import logging
import logging.handlers

# See https://docs.python.org/3/howto/logging-cookbook.html
# create parent logger
PARENTLOGGER = logging.getLogger()
PARENTLOGGER.setLevel (logging.DEBUG)
BUFFERLOGGER = logging.handlers.MemoryHandler(capacity=1000,flushLevel=logging.CRITICAL)
PARENTLOGGER.addHandler(BUFFERLOGGER)
from .logs import start_logging
start_logging(PARENTLOGGER, BUFFERLOGGER)
from .constants import *
from .utilities import *
