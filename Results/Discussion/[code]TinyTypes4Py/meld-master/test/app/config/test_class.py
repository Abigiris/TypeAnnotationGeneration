import unittest
from tempfile import gettempdir
from pathlib import Path
import json

from meld.app.config.load import load_json, load_python
from meld.app.config import Config

class ConfigLoader(unittest.TestCase):
	def testPythonExt(self):
		loader = Config._get_loader('.py')
		self.assertIs(loader, load_python)
	def testJSONExt(self):
		loader = Config._get_loader('.json')
		self.assertIs(loader, load_json)
	def testUnsupportedExtension(self):
		with self.assertRaises(OSError):
			Config._get_loader('.html')

class ConfigConstructor(unittest.TestCase):
	config_path = Path(gettempdir(), 'config.json')  #TODO: Change to pyfakefs
	content = {'foo': 'bar'}
	@classmethod
	def setUpClass(cls):
		if cls.config_path.exists():
			cls.config_path.unlink()
		
		cls.config_path.write_text(json.dumps(cls.content))

	@classmethod
	def tearDownClass(cls):
		if cls.config_path.exists():
			cls.config_path.unlink()

	def setUp(self):
		try:
			self.config = Config(self.config_path)
		except Exception as e:
			self.fail(f'Failed to setup: {e}')

	def assertHasAttr(self, obj, attr, msg=None):
		"""
		Tests whether an object has an attribute
		"""
		if not hasattr(obj, attr):
			if msg:
				self.fail(msg)
			else:
				self.fail(f'{obj} show have the attribute {attr}')
	def testHasPathAttribute(self):
		self.assertHasAttr(self.config, 'path')
	def testHasExtAttribute(self):
		self.assertHasAttr(self.config, 'ext')
	def testHasContentAttribute(self):
		self.assertHasAttr(self.config, 'content')
	def testPathAttributeIsPathlibPath(self):
		self.assertIsInstance(self.config.path, Path)
	def testExtAttributeIsStr(self):
		self.assertIsInstance(self.config.ext, str)
	def testContentAttributeIsDict(self):
		self.assertIsInstance(self.config.content, dict)
	def testContentShouldBeLoaded(self):
		"""
		The content of the specified config path should automatically be loaded
		"""
		self.assertDictEqual(self.content, self.config.content)