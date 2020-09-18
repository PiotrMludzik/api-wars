# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                           Star Wars API requests & responses
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import requests


SWAPI_PAGINATION_NUMBER = 10
SWAPI_ROOT_URL = 'https://swapi.dev/api/'


def get_data(url_request: str) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    return requests.get(SWAPI_ROOT_URL + url_request).json()
