import unittest
import json
from tempfile import gettempdir  # TODO: change to pyfakefs
from pathlib import Path

from meld.app.config.load import load_json, load_python


class JSONConfig(unittest.TestCase):
    def setUp(self):
        self.path = Path(gettempdir(), 'testConfig.json')
        self.path.touch()

    def tearDown(self):
        if self.path.exists():
            self.path.unlink()

    def testPathIsString(self):
        content = {
            "string": "This is a string",
            "int": 2,
            "float": 1.0,
            "list": ['foo', 3, {'hello': 'world'}, [], 3.14],
            "Null": None,
            "nested": {
                'pi': 3.14
            }
        }
        self.path.write_text(json.dumps(content))
        try:
            self.assertDictEqual(content, load_json(str(self.path)))
        except Exception as e:
            self.fail(e)

    def testPathIsPathlibPath(self):
        content = {}
        self.path.write_text(json.dumps(content))
        try:
            self.assertDictEqual(content, load_json(Path(self.path)))
        except Exception as e:
            self.fail(e)


class PythonConfig(unittest.TestCase):
    def setUp(self):
        self.path = Path(gettempdir(), 'testConfig.py')
        self.path.touch()

    def tearDown(self):
        if self.path.exists():
            self.path.unlink()

    def testPathIsString(self):
        config = {'foo': 'bar'}
        content = f"""
config = {config}
"""
        self.path.write_text(content)
        try:
            self.assertDictEqual(config, load_python(str(self.path)))
        except Exception as e:
            self.fail(e)

    def testPathIsPathlibPath(self):
        config = {'foo': 'bar'}
        content = f"""
config = {config}
"""
        self.path.write_text(content)
        try:
            self.assertDictEqual(config, load_python(Path(self.path)))
        except Exception as e:
            self.fail(e)

    def testDifferentVarName(self):
        var_name = 'some_variable'
        config = {'foo': 'bar'}
        content = f"""
{var_name} = {config}
"""
        self.path.write_text(content)
        try:
            self.assertDictEqual(config, load_python(
                Path(self.path), attribute=var_name))
        except Exception as e:
            self.fail(e)
