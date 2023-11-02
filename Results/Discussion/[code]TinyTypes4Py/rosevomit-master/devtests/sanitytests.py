# This Python file uses the following encoding: utf-8
"""Contains tests using 'unittest' module."""
from io import StringIO
import random
import sys
import unittest

# Import Rosevomit for testing
from context import rosevomit
from rosevomit import core, programlogic

# ---------- Helper functions ----------
def test_string_generation (testcaseself, keyword: str):
    """Do we get the number of items we expect?"""
    number_names_to_generate = random.randint (2, 200)
    old_stdout = sys.stdout

    test_stdout = StringIO()  # io.StringIO is in-memory stream for text I/O.
    sys.stdout = test_stdout  # Redirecting stdout to stream.
    rosevomit.programlogic.logiccontroller.generate_names (keyword, number_names_to_generate)  # Actually running test

    sys.stdout = old_stdout  # Resetting stdout to print to terminal again
    result = test_stdout.getvalue()  # Reading the test results from memory
    names_generated = result.split('\n')
    if names_generated[-1] == "":   # Sometimes the results end with a blank line.
        del names_generated[-1]     # We get rid of that.
    else:
        pass
    testcaseself.assertEqual (number_names_to_generate, len (names_generated))


def validate_string_cleaning (testcaseself, target_string: str):
    """Do we find forbidden characters?"""
    bad_characters = ("\n", "\r")
    for item in bad_characters:
        testcaseself.assertNotIn (item, target_string)
    # Checking for beginning or ending spaces
    firstcharacter = target_string[0]
    lastcharacter = target_string[-1]
    testcaseself.assertNotEqual (firstcharacter, " ")
    testcaseself.assertNotEqual (lastcharacter, " ")


# ---------- Unit tests ----------
class ConstantTests (unittest.TestCase):
    """Testing the values of constants from rosevomit.core.constants"""
    def test_obvious (self):
        """Testing that I know how to write a test."""
        self.assertTrue (rosevomit.core.constants.SEE_ROSA_RUN)

    def test_constant_types (self):
        """Are the constants of the correct type?"""
        self.assertIsInstance (rosevomit.core.constants.SEE_ROSA_RUN, bool)
        self.assertIsInstance (rosevomit.core.constants.CLI_DIRECTORY_NAME, str)
        self.assertIsInstance (rosevomit.core.constants.LOGIC_DIRECTORY_NAME, str)
        self.assertIsInstance (rosevomit.core.constants.DATA_DIRECTORY_NAME, str)
        self.assertIsInstance (rosevomit.core.constants.TEMP_DIRECTORY_NAME, str)
        self.assertIsInstance (rosevomit.core.constants.SAVE_DIRECTORY_NAME, str)
        self.assertIsInstance (rosevomit.core.constants.REGEXES_YES, list)
        self.assertIsInstance (rosevomit.core.constants.REGEXES_NO, list)
        self.assertIsInstance (rosevomit.core.constants.REGEXES_OPT, list)

    def test_constants_not_empty (self):
        """Are the constants empty?"""
        # In Python, empty sequences return as False and non-empty sequences return as True
        self.assertTrue (rosevomit.core.constants.CLI_DIRECTORY_NAME)
        self.assertTrue (rosevomit.core.constants.LOGIC_DIRECTORY_NAME)
        self.assertTrue (rosevomit.core.constants.DATA_DIRECTORY_NAME)
        self.assertTrue (rosevomit.core.constants.TEMP_DIRECTORY_NAME)
        self.assertTrue (rosevomit.core.constants.SAVE_DIRECTORY_NAME)
        self.assertTrue (rosevomit.core.constants.REGEXES_YES)
        self.assertTrue (rosevomit.core.constants.REGEXES_NO)
        self.assertTrue (rosevomit.core.constants.REGEXES_OPT)


class LowLevelTests (unittest.TestCase):
    """Testing various low level functions in Rosevomit."""
    def test_func_one_file (self):
        """Does one_file() return a string without newlines and spaces?"""
        result = rosevomit.programlogic.randomname.one_file ("SampleData.txt")
        # Checking that it returns a string
        self.assertIsInstance (result, str)
        validate_string_cleaning (self, result)

    def test_func_two_files (self):
        """Does two_files() return a string without newlines and spaces?"""
        result = rosevomit.programlogic.randomname.two_files ("SampleData.txt", "SampleData2.txt")
        # Checking that it returns a string
        self.assertIsInstance (result, str)
        validate_string_cleaning (self, result)


class UtilityTests (unittest.TestCase):
    """Testing various functions from the utilities module."""
    def test_angle_sanity_check_int (self):
        """Do we ever get angles larger than 360 degrees? (integer version)"""
        test_integers = []
        while len (test_integers) < 50:
            random_integer = random.randint (-1000000, 1000000)
            test_integers.append (random_integer)
        for item in test_integers:
            result = rosevomit.core.utilities.angle_sanity_check (item)
            self.assertTrue (0 <= result < 360)

    def test_angle_sanity_check_float (self):
        """Do we ever get angles larger than 360 degrees? (float version)"""
        test_floats = []
        while len (test_floats) < 50:
            random_float = random.uniform (-1000000, 1000000)
            test_floats.append (random_float)
        for item in test_floats:
            result = rosevomit.core.utilities.angle_sanity_check (item)
            self.assertTrue (0 <= result < 360)


class NameGenerationTests (unittest.TestCase):
    """Testing Rosevomit's name generation feature."""
    def test_name_generation (self):
        """Do we get the number of names we expect?"""
        keyword_list = ["first", "firstfemale", "firstmale", "last", "full", "fullfemale", "fullmale"]
        for keyword in keyword_list:
            test_string_generation (self, keyword)


if __name__ == "__main__":
    unittest.main()
