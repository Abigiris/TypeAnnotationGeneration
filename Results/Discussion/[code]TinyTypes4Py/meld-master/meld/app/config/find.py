import json
from pathlib import Path

from click import get_app_dir

from meld import logger, app_data_dir, __title__ as app_name
from .load import SUPPORTED_FORMATS
from .base_config import BASE_CONFIG


def _find_config_in_folder(folder: str) -> str:
	folder = Path(folder)
	for config_ext in SUPPORTED_FORMATS:
		config_path = folder.joinpath(f'config{config_ext}')
		if config_path.exists():
			return config_path

def _generate_base_config(config_dir: str) -> str:
	config_path = Path(config_dir).joinpath('config.json')
	config_path.write_text(json.dumps(BASE_CONFIG, indent=4, sort_keys=True))
	return config_path

def find_config_path() -> str:
	"""
	Finds the path to the application config

	The config priority is as follows in decending order
		${HOME}/.config/meld/config.<ext>
		${LOCALAPPDATA}/meld/config.<ext>

	Note that on windows, this both these locations should be the same
	"""

	# ~/.config/<app_name>
	user_config_dir = Path(get_app_dir(app_name, roaming=False))

	logger.debug('Finding user config')
	config_path = _find_config_in_folder(user_config_dir)
	if config_path:
		logger.debug(f'Found user config at: {config_path}')
		return config_path
	logger.debug('No user config found')

	logger.debug('Finding base config')
	config_path = _find_config_in_folder(app_data_dir)
	if config_path:
		logger.debug(f'Found base config at: {config_path}')
		return config_path
	logger.debug('No base config found')
	
	logger.debug('Generating base config')
	config_path = _generate_base_config(app_data_dir)
	
	return config_path
