import click

from meld import logger
from .show import show as show_config


@click.group()
def config():
    """
    Top-level config CLI
    """
    logger.debug("Started 'config' CLI")

@config.command()
@click.option('--pretty', is_flag=True, help='Multiline print and sort keys')
@click.pass_context
def show(ctx, pretty):
    """
    Shows the config in console
    """

    logger.debug("Started 'show' CLI")

    # get all the args for debugging purposes
    command_args = {arg: value for arg,
                    value in locals().items() if arg is not 'ctx'}

    logger.debug(f"Arguments: {command_args}")
    logger.debug(f'Context variables: {ctx.obj}')
    try:
        logger.debug('Showing config')
        show_config(ctx.obj['config'].content, pretty)
    except Exception as e:
        logger.error(f'Failed to show config: {e}')
    else:
        logger.debug('Successfully show config')

@config.command()
@click.pass_context
def path(ctx):
    """
    Shows the path to the config file loaded
    """

    logger.debug("Started 'path' CLI")

    # get all the args for debugging purposes
    command_args = {arg: value for arg,
                    value in locals().items() if arg is not 'ctx'}

    logger.debug(f"Arguments: {command_args}")
    logger.debug(f'Context variables: {ctx.obj}')
    try:
        logger.debug('Showing config path')
        click.echo(ctx.obj['config'].path)
    except Exception as e:
        logger.error(f'Failed to show config path: {e}')
    else:
        logger.debug('Successfully show config path')
