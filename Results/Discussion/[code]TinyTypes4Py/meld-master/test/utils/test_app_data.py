import unittest
from pathlib import Path, WindowsPath, PosixPath
import importlib
import os.path
from tempfile import gettempdir  # TODO: Change to pyfakefs

import meld
import meld.utils.app_data
app_data_dir = meld.utils.app_data.app_data_dir

def isPosix():
	tmp_path = Path(gettempdir())
	if isinstance(tmp_path, PosixPath):
		return True
	elif isinstance(tmp_path, WindowsPath):
		return False
	raise OSError('idk what os this is')
	

@unittest.skipUnless(isPosix(), 'System is not Posix')
class PosixAppDataDir(unittest.TestCase):
	def setUp(self):
		self.tmp_name = app_data_dir.parent.joinpath(f'{meld.__title__}.tmp')

		try:
			if app_data_dir.exists():
				app_data_dir.rename(self.tmp_name)
			self.assertFalse(app_data_dir.exists(), 'Failed to delete existing app_dir')
			importlib.reload(meld.utils.app_data)
		except Exception:
			self.fail('setup failed')
	def tearDown(self):
		if app_data_dir.exists():
			app_data_dir.rmdir()
		if self.tmp_name.exists():
			self.tmp_name.rename(app_data_dir)

	def testType(self):
		self.assertIsInstance(app_data_dir, Path)
	def testPath(self):
		expected_path = os.path.expanduser(f'~/.local/share/{meld.__title__}')
		self.assertEqual(expected_path, str(app_data_dir))
	def testMkdir(self):
		""" Module should automatically create the app directory if not exists """
		app_data_dir.rmdir()
		importlib.reload(meld.utils.app_data)
		self.assertTrue(app_data_dir.exists(), 'failed to create app dir')
		self.assertTrue(app_data_dir.is_dir(), 'app_data_dir is not a dir')

@unittest.skipUnless(not isPosix(), 'System is not Windows')
class WindowsAppDataDir(unittest.TestCase):
	def setUp(self):
		self.tmp_name = app_data_dir.parent.joinpath(f'{meld.__title__}.tmp')

		try:
			if app_data_dir.exists():
				app_data_dir.rename(self.tmp_name)
			self.assertFalse(app_data_dir.exists(), 'Failed to delete existing app_dir')
			importlib.reload(meld.utils.app_data)
		except Exception:
			self.fail('setup failed')
	def tearDown(self):
		if app_data_dir.exists():
			app_data_dir.rmdir()
		if self.tmp_name.exists():
			self.tmp_name.rename(app_data_dir)

	def testType(self):
		self.assertIsInstance(app_data_dir, Path)
	def testPath(self):
		expected_path = os.path.expandvars(f'%LOCALAPPDATA%/{meld.__title__}')
		self.assertEqual(expected_path, str(app_data_dir))
	def testMkdir(self):
		""" Module should automatically create the app directory if not exists """
		app_data_dir.rmdir()
		importlib.reload(meld.utils.app_data)
		self.assertTrue(app_data_dir.exists(), 'failed to create app dir')
		self.assertTrue(app_data_dir.is_dir(), 'app_data_dir is not a dir')
