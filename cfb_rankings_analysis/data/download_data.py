import cfbd
from cfbd.rest import ApiException
from dotenv import load_dotenv
import os


def main():
    download_betting_lines()


def download_betting_lines():
    # Configure API key authorization: ApiKeyAuth
    configuration = configure_cfbd_api_auth()

    # create an instance of the API class
    api_instance = cfbd.BettingApi(cfbd.ApiClient(configuration))
    year = 2022 # int | Year/season filter for games (optional)
    week = 4 # int | Week filter (optional)
    season_type = 'regular' # str | Season type filter (regular or postseason) (optional) (default to regular)
    team = 'Tennessee' # str | Team (optional)

    try:
        # Betting lines
        api_response = api_instance.get_lines(year=year, week=week, season_type=season_type, team=team)
        print(api_response)
    except ApiException as e:
        print("Exception when calling BettingApi->get_lines: %s\n" % e)


def configure_cfbd_api_auth() -> cfbd.Configuration:
    """Configure API key authorization: ApiKeyAuth for College Football Data API"""
    configuration = cfbd.Configuration()
    configuration.api_key['Authorization'] = get_environment_variable("cfbd_api_key")
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    return configuration


def get_environment_variable(env_var: str) -> str:
    """Return the value associated with an environment variable"""
    load_dotenv()
    try:
        value = os.getenv(env_var)
        if value is None:
            raise TypeError("Environment variable not gotten")
    except TypeError as e:
        print(f"{e}: Environment variable '{env_var}' does not exist.")
    else:
        return value


if __name__ == "__main__":
    main()
