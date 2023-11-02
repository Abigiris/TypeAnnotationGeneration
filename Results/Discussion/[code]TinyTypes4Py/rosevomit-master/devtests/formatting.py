# This Python file uses the following encoding: utf-8
"""This file contains functions for the formatting of the the test results files."""


def line(char: str = "_", newline: bool = False) -> None:
    """Prints a character 70 times, with an optional preceding newline."""
    if newline is True:
        print ()
    if len(char) == 1:
        print (char * 70)
    else:
        raise ValueError(f"The parameter 'char' must be a string that is one character long, not {len(char)} characters long!")


def header(text: str) -> None:
    """Prints a centered, all-uppercase header for the unittest log files. Tries to center the 'headertext' for a 70-character column width. """
    if not str.isupper(text):
        text = str.upper(text)
    num_spaces = int ((70 - len (text)) / 2)
    print (" " * num_spaces, text, " " * num_spaces, sep="")
