import json
import importlib.util

SUPPORTED_FORMATS = ['.json', '.py']

def load_json(config_path):
	with open(config_path, 'r') as f:
		return json.load(f)

def load_python(config_path, attribute='config'):
	# This imports a module using an absolute path
	spec = importlib.util.spec_from_file_location(
		"_config", str(config_path))
	config_module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(config_module)

	return getattr(config_module, attribute)