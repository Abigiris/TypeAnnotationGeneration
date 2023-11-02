import click

from .main import main

@click.command(name='_template')
@click.pass_context
@click.option('--option')
def cli(ctx, option):
	main()