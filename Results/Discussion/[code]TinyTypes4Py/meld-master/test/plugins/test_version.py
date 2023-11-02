import unittest
import sys
import io
from contextlib import contextmanager

import click.testing

from meld import __version__ as version
from meld.plugins.version.main import main
from meld.plugins.version.cli import version as cli

@contextmanager
def captured_output():
	""" Captures stdout and stderr in a with block """
	# Refer to:
	# https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
	new_out, new_err = io.StringIO(), io.StringIO()
	old_out, old_err = sys.stdout, sys.stderr
	try:
		sys.stdout, sys.stderr = new_out, new_err
		yield sys.stdout, sys.stderr
	finally:
		sys.stdout, sys.stderr = old_out, old_err

class Main(unittest.TestCase):
	def testConsoleOutput(self):
		with captured_output() as (out, _):
			main()
		output = out.getvalue()
		self.assertEqual(version + '\n', output)

class CLI(unittest.TestCase):
	def testCLI(self):
		runner = click.testing.CliRunner()
		result = runner.invoke(cli)
		self.assertEqual(result.exit_code, 0)
		self.assertIn(version + '\n', result.output)