# This Python file uses the following encoding: utf-8
"""Contains miscellaneous functions."""
import os
import pathlib
import sys
import traceback


def make_name_unique (basename: str) -> str:
    """If the basename isn't unique within the current working directory, this function adds an integer to the end of the basename and increments it until it becomes unique."""
    number = 1
    name = basename
    while os.path.exists (name) is True:
        number = number + 1
        name = basename + "-" + str(number)
    return name


def get_cwd_name_only():
    """Returns only the folder name of the current working directory, not the full path."""
    _cwd = pathlib.Path.cwd()
    _path_split = os.path.split(_cwd)
    return _path_split[-1]

# THANKS: https://stackoverflow.com/questions/2828953/silence-the-stdout-of-a-function-in-python-without-trashing-sys-stdout-and-resto/40054132#40054132
class Suppressor(object):
    """Silences stdout of a function without wrapping a function all.

    Usage:
    with Suppressor():
        DoMyFunction(*args,**kwargs)
    """
    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self

    def __exit__(self, type, value, traceback):
        sys.stdout = self.stdout
        if type is not None:
            # Do normal exception handling
            raise

    def write(self, x):
        pass
