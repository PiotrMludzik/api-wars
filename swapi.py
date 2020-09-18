# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                           Star Wars API requests & responses
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import requests


PAGINATION_NUMBER = 10
ROOT_URL = 'https://swapi.dev/api/'


def get_data(url_request: str) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    return requests.get(ROOT_URL + url_request).json()
