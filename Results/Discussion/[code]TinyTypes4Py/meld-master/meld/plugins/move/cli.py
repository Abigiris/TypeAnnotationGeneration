import click

from .main import main

@click.command(name='move')
@click.pass_context
@click.option('-s', '--set-id', type=int, required=True)
@click.option('-f', '--format', 'path_format', r'${set_name}/${file_name}')
@click.option('-p', '--preprocess', help='Preprocessing script to run')
def move(ctx, set_id, path_format):
    """
    Move files using the specified format
    """
    click.echo('this is the move command')
    main()