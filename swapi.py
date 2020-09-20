# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                           Star Wars API requests & responses
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import requests


PAGINATION_NUMBER = 10
ROOT_URL = 'https://swapi.dev/api/'  # root the https API adress
URL = ROOT_URL[8:]  # without the protocol sygnature (https://)


def get_data(url_request: str) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    return requests.get(ROOT_URL + url_request).json()


def get_data_name(url_request: str) -> str:
    """ Sends a request to the SWAPI API and returns the name of a specific thing. """
    all_data = requests.get(url_request).json()
    return all_data['name']


def has_api_url(string: str) -> bool:
    """ Returns True if string contains the http API address. """
    return True if string.find(URL) != -1 else False
