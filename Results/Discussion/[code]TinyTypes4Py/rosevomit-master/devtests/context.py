# This Python file uses the following encoding: utf-8
# -- devtests/context.py --
# The devtest module needs to import Rosevomit to test it. To do this, we use an explicit path modification to resolve the path properly.
# For more information: https://docs.python-guide.org/writing/structure/#test-suite
"""The devtest module needs to import Rosevomit to test it. To do this, we use an explicit path modification to resolve the path properly."""
import os
import sys

# We add the current directory's parent directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
# TO SEE IF THIS IS WORKING, UNCOMMENT ME
# and put the first block of code above the 'sys.path...' line.

print ("Before:")
for p in sys.path:
    print(p)
print ()

print ("After:")
for p in sys.path:
    print(p)
print ()
"""

import rosevomit
