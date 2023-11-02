from pathlib import Path

import click

def main(filter_:str ='all'):
	import meld.plugins as plugins  # This is to prevent cyclic import

	plugin_list = {
		'all': plugins.builtin_plugins + plugins.user_plugins,
		'builtin': plugins.builtin_plugins,
		'user': plugins.user_plugins
	}[filter_]
	for plugin in plugin_list:
		p = Path(plugin.__file__)
		click.echo(str(p))