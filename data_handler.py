# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                data handler functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import locale
import requests
import constants as c


# --------------------------------------------------- data handling ---------------------------------------------------

def planets_prepare_html_data(page_number: int = 1) -> list:
    """ Returns only the necessary data about the planets """
    raw_planets_data = planets_get_data(page_number)

    prepared_planets_data = []
    for raw_planet in raw_planets_data:
        prepared_planet = {}
        for key in c.PLANETS_COLUMN_ORDER:
            prepared_planet[key] = raw_planet[key]
        prepared_planets_data.append(prepared_planet)

    return planets_format_html_data(prepared_planets_data)


def planets_format_html_data(planets_data: list) -> list:
    """ Returns formatted the planets' data """
    def format_diameter(data):
        return '{:n} km'.format(int(data))

    def format_water(data):
        if data == 'unknown':
            return data
        if data == '0':
            return 'no water'

        return f'{data}%'

    def format_population(data):
        return '{:n} people'.format(int(data)) if data != 'unknown' else data

    # ------------- planets_format_html_data() -------------
    locale.setlocale(locale.LC_ALL, '')

    for planet in planets_data:
        planet[c.KEY_PLANETS_DIAMETER] = format_diameter(planet[c.KEY_PLANETS_DIAMETER])
        planet[c.KEY_PLANETS_WATER] = format_water(planet[c.KEY_PLANETS_WATER])
        planet[c.KEY_PLANETS_POPULATION] = format_population(planet[c.KEY_PLANETS_POPULATION])

    return planets_data


def planets_get_data(page_number: int = 1) -> list:
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
