import logging

import click

from meld import logger
import meld.database
from meld.app.config import find_config_path, Config
import meld.app.utils as utils


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.pass_context
@click.option('--log-level', default='info', type=click.Choice(
    ['debug', 'info', 'warning', 'error', 'critical', 'quiet']
))
@click.option('-c', '--config', 'config_path',
              type=click.Path(exists=True, dir_okay=False,
                              readable=True, resolve_path=True),
              help='User configuration file')
@click.option('-d', '--database', 'database_path',
              type=click.Path(exists=False), help='Path to database')
def cli(ctx, log_level, config_path, database_path):
    """
    Main cli function
    """

    # get all the args for debugging purposes
    command_args = {arg: value for arg,
                    value in locals().items() if arg is not 'ctx'}

    # Setup loggers
    logging.getLogger().setLevel(logging.DEBUG)  # make sure all logs written
    # Change stream handler verbosity to given log-level
    logger.handlers[0].setLevel({
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
        'quiet': 51  # any number greater than 50 (logging.CRITICAL) would work
    }[log_level])

    logger.debug('Started main CLI')
    logger.debug(f'Arguments: {command_args}')

    # This allows us to pass the ctx variable to subcommands as a dict
    # The ensure_object only initializes the type of object to forward
    # For instance, in the parent command, we can encode
    #   ctx.obj['hello'] = 'world'
    # and in a subcommand, we can access the variable using
    #   ctx.obj['hello'] == 'world'
    # The context contains info on all parent contexts and can be accessed
    # using the click.pass_context decorator
    logger.debug('Initializing context')
    ctx.ensure_object(dict)
    logger.debug(f'Context variables: {ctx.obj}')

    if not config_path:
        logger.debug('No config specified, finding config')
        config_path = find_config_path()

    logger.debug(f'Loading config: {config_path}')
    config = Config(config_path)
    logger.debug(f'Loaded config: {config.content}')
    logger.debug('Adding config to context')
    ctx.obj['config'] = config

    logger.debug('Initializing database')
    if not database_path:
        logger.debug('No database specified, using database from config')
        database_path = config.content['database']
    logger.debug(f'Using database: {database_path}')
    tables = [getattr(meld.database.tables, tbl_name)
              for tbl_name in meld.database.tables.__all__]
    logger.debug(f'Tables loaded: {[tbl.name for tbl in tables]}')

    database = meld.database.Database(database_path, tables)
    logger.debug('Adding database to context')
    ctx.obj['database'] = database
    logger.debug('Creating tables')
    database.createTables(database.conn)  # create tables and commit

    logger.debug('Finished executing main CLI')


# Add subcommands that are not private
for plugin in utils.plugins.get_plugin_with_attr('cli'):
    command = plugin.cli
    if command.name[0] != '_':
        cli.add_command(command)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
