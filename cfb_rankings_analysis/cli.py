import click


class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', '-v', is_flag=True, help="Print more logging messages.")
@pass_config
def cli(config, verbose):
    config.verbose = verbose


@cli.command()
@pass_config
def say_hello(config):
    """Print a simple 'Hello World!' to the console."""
    if config.verbose:
        click.echo("We are in verbose mode.")
    click.echo('Hello World!')
