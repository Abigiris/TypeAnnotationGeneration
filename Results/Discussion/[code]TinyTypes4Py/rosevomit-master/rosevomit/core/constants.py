# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# constants.py
# rosevomit.core.constants
# ___________________________________________________________________
"""This file contains constants that will be used throughout Rosevomit."""
from pathlib import Path
import re

from core import _dynamic_constants, logs

_CONSTANTSLOGGER = logs.BaseLogger (__name__)

# ---------- STATIC CONSTANTS ----------
# These constants are explicitly defined in the code.

SEE_ROSA_RUN: bool = True

_CORE_DIRECTORY_NAME = "core"
LOG_DIRECTORY_NAME = "core/logdata"
CLI_DIRECTORY_NAME = "programcli"
LOGIC_DIRECTORY_NAME = "programlogic"
DATA_DIRECTORY_NAME = "programdata"
TEMP_DIRECTORY_NAME = "temp"
SAVE_DIRECTORY_NAME = "saved"

# --- Lists of RegEx for parsing user input ---
REGEXES_YES: list = [
    re.compile(r"^[Y][ES]*$", flags=re.IGNORECASE),
]
REGEXES_NO: list = [
    re.compile(r"^[N][O]*$", flags=re.IGNORECASE),
]
REGEXES_OPT: list = [
    re.compile(r"^[G][IME]*$", flags=re.IGNORECASE),
    re.compile(r"^[M][ORE]*", flags=re.IGNORECASE),
    re.compile(r"^[O][PTIONS]*", flags=re.IGNORECASE),
    re.compile(r"^[G][IME]*\s*[M][ORE]*\s*[O][PTIONS]*$", flags=re.IGNORECASE),
]
# Dear future self,
# Yeah, I just learned about regular expressions. You got a problem with that?
#   Love, Your(past)self


# ---------- DYNAMIC CONSTANTS ----------
# There are some constants whose values are not known in advance and so must be generated when the program starts.

# --- Directory Paths and PurePaths ---
_CORE_DIRECTORY_PATH: Path = _dynamic_constants.get_critical_directory (_CORE_DIRECTORY_NAME)
LOG_DIRECTORY_PATH: Path = _dynamic_constants.get_critical_directory (LOG_DIRECTORY_NAME)
CLI_DIRECTORY_PATH: Path = _dynamic_constants.get_critical_directory (CLI_DIRECTORY_NAME)
LOGIC_DIRECTORY_PATH: Path = _dynamic_constants.get_critical_directory (LOGIC_DIRECTORY_NAME)
DATA_DIRECTORY_PATH: Path = _dynamic_constants.get_critical_directory (DATA_DIRECTORY_NAME)
TEMP_DIRECTORY_PATH: Path = _dynamic_constants.get_noncritical_directory (TEMP_DIRECTORY_NAME)
SAVE_DIRECTORY_PATH: Path = _dynamic_constants.get_noncritical_directory (SAVE_DIRECTORY_NAME)

# --- Version numbers ---
MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION, IS_DEVBUILD = _dynamic_constants.get_version_number (_CORE_DIRECTORY_PATH)
