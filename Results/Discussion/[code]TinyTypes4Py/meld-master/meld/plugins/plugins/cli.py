from pathlib import Path

import click

from meld import logger
from .list_ import main as list_plugins

@click.group(name="plugins", help="Manage plugins")
def cli():
    logger.debug("Started plugin CLI")


@cli.command(name="list", help="List all plugins installed")
@click.option(
    "-f",
    "--filter",
    "filter_",
    type=click.Choice(["all", "builtin", "user"]),
    default="all",
)
def list_(filter_):
	logger.debug('Started plugin list CLI')
	list_plugins(filter_)
