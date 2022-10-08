from cfb_rankings_analysis.data.download_data import (
    configure_cfbd_api_auth, get_environment_variable
)
import cfbd


def test_configure_cfbd_api_auth():
    configuration = configure_cfbd_api_auth()

    assert type(configuration) == cfbd.configuration.Configuration
    assert configuration.api_key_prefix.get("Authorization") == "Bearer"
    assert isinstance(configuration.api_key.get("Authorization"), str)


def test_get_environment_variable():
    assert get_environment_variable("test_env") == "top_secret_info"
