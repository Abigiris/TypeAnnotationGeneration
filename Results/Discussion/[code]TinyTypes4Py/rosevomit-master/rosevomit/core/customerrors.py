# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# customerrors.py
# rosevomit.core.customerrors
# ___________________________________________________________________
"""Currently a placeholder file."""
from core import logs

_CUSTOMERRORSLOGGER = logs.BaseLogger (__name__)


class RealityError(Exception):
    """These things should not happen.

    Upon __init__, pass *args and **kwargs to Exception (superclass).

    Parameters
    ----------
    *args
        A varying number of positional arguments.
    **kwargs
        A varying number of named (keyworded) arguments.
    """
    def __init__ (self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
