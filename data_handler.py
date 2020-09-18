# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                data handler functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import swapi


# --------------------------------------------------- data handlers ---------------------------------------------------

def subject_get_data(subject: str, page_number: int) -> dict:
    """ Gets the subject data. """
    data = swapi.get_data(f'{subject}/?page={page_number}')

    # error handling
    if 'detail' in data and data['detail'] == 'Not found':
        raise ValueError(f'Page {page_number} with list of the {subject} not found.')

    return data


def subject_prepare_data(subject: str, raw_data: dict) -> list:
    """ Returns only the necessary data for a given subject. """
    def get_needed_data(subject: str) -> list:
        if subject == c.SUBJECT.PLANETS:
            needed_data = c.DATA.PLANETS
        else:
            raise ValueError(f'Needed data for {subject} not found.')

        return needed_data

    # ------------- subject_prepare_data() -------------
    needed_data = get_needed_data(subject)
    prepared_data = []
    for raw_item in raw_data:
        prepared_item = {}
        for key in needed_data:
            prepared_item[key] = raw_item[key]
        prepared_data.append(prepared_item)

    return prepared_data


def subject_format_data(subject: str, data: list) -> list:
    """ Returns formatted the subject data. """
    import locale

    def format_diameter(data):
        return '{:n} km'.format(int(data)) if data != 'unknown' else data

    def format_water(data):
        if data == 'unknown':
            return data
        if data == '0':
            return 'no water'

        return f'{data}%'

    def format_population(data):
        return '{:n} people'.format(int(data)) if data != 'unknown' else data

    # ------------- subject_format_data() -------------
    locale.setlocale(locale.LC_ALL, '')

    for item in data:
        if subject == c.SUBJECT.PLANETS:
            item[c.KEY_PLANETS_DIAMETER] = format_diameter(item[c.KEY_PLANETS_DIAMETER])
            item[c.KEY_PLANETS_WATER] = format_water(item[c.KEY_PLANETS_WATER])
            item[c.KEY_PLANETS_POPULATION] = format_population(item[c.KEY_PLANETS_POPULATION])

    return data


# ------------------------------------------------ other data handlers ------------------------------------------------

def get_page_pagination_number(items_number):
    """ Calculates the number of pages of pagination. """
    return items_number // swapi.PAGINATION_NUMBER
