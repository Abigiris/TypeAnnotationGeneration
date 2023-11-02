# This Python file uses the following encoding: utf-8
# ___________________________________________________________________
# randomname.py
# rosevomit.programlogic.randomname
# ___________________________________________________________________
"""A file that contains functions for randomly generating names."""

import os
import random

try:
    from core import directories, logs
except ImportError:  # for external unit testing
    from rosevomit.core import directories


_RANDOMNAMELOGGER = logs.BaseLogger (__name__)


def one_file (ARG_file1) -> str:
    """A function that returns one random line from a text file 'ARG_file1'.

    Parameters
    ----------
    ARG_file
        The file to draw a random line from.

    Returns
    -------
    str
        A random line from 'ARG_file'.
    """
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    with open (ARG_file1, 'r') as filedata:
        contents = filedata.readlines()
        contents = [item.strip() for item in contents]  # strips newline characters ('\n') and spaces
        return random.choice (contents)


def two_files (ARG_file1, ARG_file2) -> str:
    """A function that returns one random line from a list generated from multiple text files 'x', 'y', and so on.

    Parameters
    ----------
    ARG_file1, ARG_file2
        The files to draw a random line from.

    Returns
    -------
    str
        A random line from 'ARG_file1' or 'ARG_file2'.
    """
    data_dir = directories.get_dir("programdata")
    os.chdir (data_dir)
    filedata1 = open (ARG_file1, 'r')
    contents1 = filedata1.readlines()
    contents1 = [item.strip() for item in contents1]  # strips newline characters ('\n') and spaces
    filedata1.close()
    filedata2 = open (ARG_file2, 'r')
    contents2 = filedata2.readlines()
    contents2 = [item.strip() for item in contents2]
    filedata2.close()
    contents = contents1 + contents2
    return random.choice (contents)


def getname_firstany():
    """Returns a random first name. Accepts nothing, returns nothing."""
    result = two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
    print (result)


def getname_firstfemale():
    """Returns a random female first name. Accepts nothing, returns nothing."""
    result = one_file ("USCensusNamesFirstFemale.txt")
    print (result)


def getname_firstmale():
    """Returns a random male first name. Accepts nothing, returns nothing."""
    result = one_file ("USCensusNamesFirstMale.txt")
    print (result)


def getname_lastany():
    """Returns a random last name. Accepts nothing, returns nothing."""
    result = one_file ("USCensusNamesLast.txt")
    print (result)


def getname_fullany():
    """Returns a random full name. Accepts nothing, returns nothing."""
    firstname = two_files ("USCensusNamesFirstFemale.txt", "USCensusNamesFirstMale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)


def getname_fullfemale():
    """Returns a random female full name. Accepts nothing, returns nothing."""
    firstname = one_file ("USCensusNamesFirstFemale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)


def getname_fullmale():
    """Prints a random male full name. Accepts nothing, returns nothing."""
    firstname = one_file ("USCensusNamesFirstMale.txt")
    lastname = one_file ("USCensusNamesLast.txt")
    result = firstname + lastname
    print (result)
