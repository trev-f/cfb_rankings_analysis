import cfbd
from cfbd.rest import ApiException
from dotenv import load_dotenv
import os


def main():
    print("This script downloads external data.")


def download_elo():
    # Configure API key authorization: ApiKeyAuth
    configuration = configure_cfbd_api_auth()

    # create an instance of the API class
    api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))

    try:
        # Betting lines
        api_response = api_instance.get_elo_ratings(year=2022, week=1, team="Tennessee")
        print(api_response)
    except ApiException as e:
        print("Exception when calling RatingsApi->get_elo_ratings: %s\n" % e)


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
