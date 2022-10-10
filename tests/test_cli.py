from click.testing import CliRunner
from cfb_rankings_analysis.cli import cli


def test_say_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ["say-hello"])
    assert result.exit_code == 0
    assert "Hello World" in result.output


def test_download_data():
    runner = CliRunner()
    result = runner.invoke(cli, ["download-data"])
    assert result.exit_code == 0
    assert "This script downloads external data." in result.output
