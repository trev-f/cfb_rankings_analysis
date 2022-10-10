import cfbd
from cfbd.rest import ApiException
from dotenv import load_dotenv
import os


def main():
    print("This script downloads external data.")


def fetch_elo(**kwargs):
    """Download historical Elo ratings"""
    configuration = configure_cfbd_api_auth()
    ratings_api_instance = cfbd.RatingsApi(cfbd.ApiClient(configuration))
    elo_response = get_elo_api_response(ratings_api_instance, **kwargs)

    return elo_response


def configure_cfbd_api_auth() -> cfbd.Configuration:
    """Configure API key authorization: ApiKeyAuth for College Football Data API"""
    configuration = cfbd.Configuration()
    configuration.api_key['Authorization'] = get_environment_variable("cfbd_api_key")
    configuration.api_key_prefix['Authorization'] = 'Bearer'

    return configuration


def get_elo_api_response(api_instance: cfbd.api.ratings_api.RatingsApi, **kwargs) -> list:
    """Get Team Historical Elo ratings"""
    try:
        elo_response = api_instance.get_elo_ratings(**kwargs)
    except ApiException as e:
        print(f"Exception when calling RatingsApi->get_elo_ratings: {e}\n")
    else:
        return elo_response


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
