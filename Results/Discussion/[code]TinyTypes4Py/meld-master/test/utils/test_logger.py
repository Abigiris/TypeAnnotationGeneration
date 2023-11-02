import unittest
from pathlib import Path, PosixPath, WindowsPath
from tempfile import gettempdir

def isPosix():
	tmp_path = Path(gettempdir())
	if isinstance(tmp_path, PosixPath):
		return True
	elif isinstance(tmp_path, WindowsPath):
		return False
	raise OSError('idk what os this is')

# TODO: Write tests
@unittest.skipUnless(isPosix(), 'This is not a Posix system')
class PosixLogDir(unittest.TestCase):
	def testType(self):
		pass
	def testPath(self):
		pass
	def testmkdir(self):
		""" Log dir should automatically be created if not exists """
		pass

class StreamHandler(unittest.TestCase):
	def testFormatter(self):
		pass

class FileHandler(unittest.TestCase):
	def testFormatter(self):
		pass
	def testFilePath(self):
		pass
	def testLogLevel(self):
		pass

class Logger(unittest.TestCase):
	def testHandlersSet(self):
		""" Should be composed of the stream and file handler """
		pass
	def testFirstHandler(self):
		""" Should be the stream handler """
		# The first handler is the stream handler for compatibility reasons
		# The main cli initializes the log-level of the first handler 
		# (assumed to be the stream handler)
		pass