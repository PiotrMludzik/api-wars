# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                           Star Wars API requests & responses
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import requests


PAGINATION_NUMBER = 10
ROOT_URL = 'https://swapi.dev/api/'  # root the https API adress


def get_data(url_request: str, full_url: bool = False) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    if not full_url:
        url_request = ROOT_URL + url_request

    return requests.get(url_request).json()


def get_data_name(url_request: str) -> str:
    """ Sends a request to the SWAPI API and returns the name of a specific thing. """
    all_data = requests.get(url_request).json()
    return all_data['name']
