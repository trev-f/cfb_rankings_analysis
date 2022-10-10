from cfb_rankings_analysis.data.download_data import (
    configure_cfbd_api_auth, get_environment_variable, fetch_elo
)
import cfbd


def test_fetch_elo():
    # test download Elo for single team
    expected_elo = cfbd.models.team_elo_rating.TeamEloRating(conference="SEC", elo=1756.0, team="Tennessee", year=2022)
    actual_elo = fetch_elo(year=2022, team="Tennessee", week=1)[0]
    assert actual_elo == expected_elo

    # test download Elo for all teams from one week
    expected_number_elos = 131
    actual_number_elos = len(fetch_elo(year=2022, week=1))
    assert actual_number_elos == expected_number_elos


def test_configure_cfbd_api_auth():
    configuration = configure_cfbd_api_auth()

    assert isinstance(configuration, cfbd.configuration.Configuration)
    assert configuration.api_key_prefix.get("Authorization") == "Bearer"
    assert isinstance(configuration.api_key.get("Authorization"), str)


def test_get_environment_variable():
    assert get_environment_variable("test_env") == "top_secret_info"
