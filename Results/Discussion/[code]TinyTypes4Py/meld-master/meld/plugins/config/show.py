from typing import Union
import json

import click

from meld.app.config import Config

def show(config: Union[dict, Config], pretty=False):
	if isinstance(config, Config):
		config = config.content
	if pretty:
		config = json.dumps(config, indent=4, sort_keys=True)
	click.echo(config)