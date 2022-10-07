import click
import logging


class Config(object):
    def __init__(self):
        self.verbose = False
        self.logger = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Print more logging messages.")
@pass_config
def cli(config, verbose):
    """Run commands from cfb_rankings_analysis module."""
    config.verbose = verbose
    config.logger = create_logger(verbose)

    config.logger.info("Start CLI program.")


@cli.command()
@pass_config
def say_hello(config):
    """Print a simple 'Hello World!' to the console."""
    config.logger.info("Say hello")

    click.echo("Hello World!")

    config.logger.info("Said hello")


def create_logger(verbose):
    # create the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create a file handler
    file_handler = logging.FileHandler(".log")
    file_handler.setLevel(logging.DEBUG)

    # create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(set_handler_level(verbose))

    # create formatter and add to handlers
    formatter = logging.Formatter(
        "%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def set_handler_level(verbose):
    if verbose:
        return logging.DEBUG
    else:
        return logging.ERROR
