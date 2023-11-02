import unittest
from tempfile import gettempdir
import json
from pathlib import Path, WindowsPath, PosixPath  # TODO: Change to pyfakefs
import os

import meld.app.config.find as test
from meld.app.config.base_config import BASE_CONFIG


def _isPosix():
	"""
	Check if we are on *nix or Windows
	"""
	path_ = Path(gettempdir())
	if isinstance(path_, PosixPath):
		return True
	elif isinstance(path_, WindowsPath):
		return False
	else:
		raise RuntimeError('IDK what OS IM ON')


class FindConfigInFolder(unittest.TestCase):
	user_config_dir = Path(os.path.expanduser('~/.config/'), 'meld')
	app_config_dir = Path(os.path.expanduser(
		'~/.local/share'), 'meld') if _isPosix() else \
		Path(os.getenv('LOCALAPPDATA'), 'meld')

	# check if config exists in the following folders
	# 	~/.config/meld/
	# 	~/.local/share/meld/  or  %APPDATA%/Local/meld/
	@classmethod
	def setUpClass(cls):
		# check to see if there is already an existing config
		cls.user_config_dir.mkdir(parents=True, exist_ok=True)
		cls.app_config_dir.mkdir(parents=True, exist_ok=True)

		for ext in test.SUPPORTED_FORMATS:
			user_config_path = cls.user_config_dir.joinpath(f'config{ext}')
			if user_config_path.exists():
				user_config_path.rename(
					cls.user_config_dir / f'config{ext}.test.backup')

			app_config_path = cls.app_config_dir.joinpath(f'config{ext}')
			if app_config_path.exists():
				app_config_path.rename(
					cls.user_config_dir / f'config{ext}.test.backup')

	@classmethod
	def tearDownClass(cls):
		# Restore existing configs
		for ext in test.SUPPORTED_FORMATS:
			user_config_path = cls.user_config_dir.joinpath(
				f'config{ext}.test.backup')
			if user_config_path.exists():
				user_config_path.rename(cls.user_config_dir / f'config{ext}')

			app_config_path = cls.app_config_dir.joinpath(
				f'config{ext}.test.backup')
			if app_config_path.exists():
				app_config_path.rename(cls.user_config_dir / f'config{ext}')

	def tearDown(self):
		# delete any generated configs
		for ext in test.SUPPORTED_FORMATS:
			user_config_path = self.user_config_dir.joinpath(
				f'config{ext}')
			if user_config_path.exists():
				user_config_path.unlink()

			app_config_path = self.app_config_dir.joinpath(
				f'config{ext}')
			if app_config_path.exists():
				app_config_path.unlink()

	def testOnlyJSONInUserFolder(self):
		user_config = Path(self.user_config_dir, 'config.json')

		user_config.touch()

		config_path = test.find_config_path()
		self.assertEqual(str(config_path), str(user_config))

	def testReturnTypeIsPath(self):
		# Setup
		try:
			config_path = test.find_config_path()
		except Exception:
			self.fail('Failed to find config')

		self.assertIsInstance(
			config_path, Path, 'Config path return value is not a pathlib Path')

	def testOnlyPyInUserFolder(self):
		user_config = Path(self.user_config_dir, 'config.py')

		user_config.touch()

		config_path = test.find_config_path()
		self.assertEqual(str(config_path), str(user_config))
	
	@unittest.skip('untested')
	def testMultipleConfigInUserFolder(self):
		pass

	def testOnlyJSONInAppFolder(self):
		app_config = Path(self.app_config_dir, 'config.json')

		app_config.touch()

		config_path = test.find_config_path()
		self.assertEqual(str(config_path), str(app_config))

	def testOnlyPyInAppFolder(self):
		app_config = Path(self.app_config_dir, 'config.py')

		app_config.touch()

		config_path = test.find_config_path()
		self.assertEqual(str(config_path), str(app_config))
	
	@unittest.skip('untested')
	def testMultipleConfigInAppFolder(self):
		pass

	def testNoConfigInAnyFolder(self):
		"""
		This should automatically generate a JSON config in app config dir
		"""

		config_path_json = self.app_config_dir.joinpath('config.json')
		if config_path_json.exists():
			config_path_json.unlink()
		config_path = test.find_config_path()
		self.assertEqual(str(config_path), str(config_path_json))

	@unittest.skip('untested')
	def testJSONConfigInAllFolders(self):
		"""
		This should return the config from the user config dir
		"""
		pass

	


class GenerateBaseConfig(unittest.TestCase):
	"""
	Creates a config file in the specified directory
	"""

	config_dir = gettempdir()

	def tearDown(self):
		test_config_path = Path(self.config_dir, 'config.json')
		if test_config_path.exists():
			test_config_path.unlink()

	def testNoErrors(self):
		"""
		Make sure config file could be written without errors
		"""
		try:
			test._generate_base_config(self.config_dir)
		except Exception:
			self.fail('Failed to write config')

	def testConfigExt(self):
		test._generate_base_config(self.config_dir)
		self.assertTrue(Path(self.config_dir, 'config.json').exists())

	def testReadConfig(self):
		"""
		Make sure config file could be read
		"""

		# Setup for this test
		try:
			test._generate_base_config(self.config_dir)
			config_path = Path(self.config_dir, 'config.json')
		except Exception:
			self.fail('Unable to setup test')

		# actual test
		try:
			config_path.read_text()
		except Exception:
			self.fail('Failed to read config')

	def testConfigContent(self):
		# Setup for this test
		try:
			test._generate_base_config(gettempdir())
			config_path = Path(gettempdir(), 'config.json')
			content = json.loads(config_path.read_text())
		except Exception:
			self.fail('Unable to setup test')

		self.assertDictEqual(content, BASE_CONFIG)
