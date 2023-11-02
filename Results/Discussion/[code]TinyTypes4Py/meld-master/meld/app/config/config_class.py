from typing import Callable, Union
from pathlib import Path
from os.path import expanduser, expandvars

from .load import SUPPORTED_FORMATS, load_json, load_python

_TypePath = Union[str, Path]

class Config:
	def __init__(self, config_path: _TypePath):
		self.path = config_path
		self.ext = self.path.suffix

		self.content = self.load()

	@property
	def path(self) -> Path:
		return self._path

	@path.setter
	def path(self, value: _TypePath):
		self._path = Path(expandvars(expanduser(value))).resolve()

	@staticmethod
	def _get_loader(ext: str) -> Callable:
		# Call the config method based on the config extension
		try:
			return {
				'.json': load_json,
				'.py': load_python
			}[ext]
		except KeyError:
			raise OSError('Config file format not supported')

	def load(self) -> dict:
		loader = self._get_loader(self.ext)
		
		return loader(self.path)