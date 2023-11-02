import unittest

from meld.app.config.base_config import BASE_CONFIG

class BaseConfig(unittest.TestCase):
	def testConfigIsDict(self):
		self.assertIsInstance(BASE_CONFIG, dict)

class ConfigSettingDatabase(unittest.TestCase):
	def testConfigHasKeyDatabase(self):
		self.assertIn('database', BASE_CONFIG)
	def testDatabaseNameIsStr(self):
		self.assertIsInstance(BASE_CONFIG['database'], str)