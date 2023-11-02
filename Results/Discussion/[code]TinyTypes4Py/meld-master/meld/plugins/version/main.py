import click
from meld import __version__ as version

def main():
	click.echo(version)