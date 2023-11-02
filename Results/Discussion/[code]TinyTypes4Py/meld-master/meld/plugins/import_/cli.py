import click

from meld import app_data_dir, logger
from .main import main, mainAsync  # TODO: Implement async
from .photos import SUPPORTED_IMAGE_FORMATS


@click.command(name='import')
@click.pass_context
@click.argument('files', type=click.Path(exists=True), nargs=-1)
@click.option('--test', is_flag=True, help='Enabling this will not commit changes to the database')
@click.option('-s', '--set-name')
@click.option('-y', '--year', default=None)
@click.option('--studio', default=None)
@click.option('-f', '--format', 'supported_formats', multiple=True, help='File formats supported',
			  default=['JPEG'], type=click.Choice(SUPPORTED_IMAGE_FORMATS, case_sensitive=False))
@click.option('--sync', help='Perform import synchronously', is_flag=True)
def cli(ctx, files, test, set_name, year, studio, supported_formats, sync):
	"""
	Inserts files into database
	"""

	logger.debug("Started 'import' CLI")
	args = {arg: value for arg, value in locals().items()
			if arg is not 'ctx'}
	logger.debug(f"Arguments: {args}")

	config = ctx.obj['config'].content
	command_config = config.get('plugins', {}).get('import', {})
	database = ctx.obj['database']

	# Override config variables with cmd arguments
	set_name = set_name or command_config.get('set_name')
	year = year or command_config.get('year')
	studio = studio or command_config.get('studio')
	supported_formats = supported_formats or command_config.get('format')

	# TODO: DELETE THIS WHEN ASYNC IS DONE
	sync = True

	# the dict comprehension cannot have locals() in the body as the scope
	# would change to the dict compr scope and not this
	_local_vars = locals()  # new local vars
	args = {arg: _local_vars[arg] for arg in args.keys()}
	logger.debug(f"Effective arguments: {args}")
	
	f = main if sync else mainAsync
	# if sync:
	# 	f = main
	# else:
	# 	raise NotImplementedError
	f(files, database, set_name, year, studio,
		 supported_formats, test=test)
