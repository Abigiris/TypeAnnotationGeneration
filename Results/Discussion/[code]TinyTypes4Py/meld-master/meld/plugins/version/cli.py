import click

from meld import logger
from .main import main

@click.command(help='Prints the application version')
def version():
    logger.debug("Started 'version' CLI")
    main()
