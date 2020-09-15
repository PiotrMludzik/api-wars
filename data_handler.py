# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                data handler functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import requests


# --------------------------------------------------- data handling ---------------------------------------------------

def get_planet_data(page_number: int = 1) -> list:
    """ Gets the planets data. """
    planets_data = swapi_get_data(f'planets/?page={page_number}')
    # error handling
    if 'detail' in planets_data and planets_data['detail'] == 'Not found':
        raise ValueError(f'Page {page_number} with list of planets not found')

    return planets_data['results']


# -------------------------------------------- SWAPI requests & responses ---------------------------------------------

def swapi_get_data(url_request: str) -> dict:
    """ Sends a request to the SWAPI API and returns the received response. """
    SWAPI_ROOT_URL = 'https://swapi.dev/api/'

    response = requests.get(SWAPI_ROOT_URL + url_request).json()
    return response
