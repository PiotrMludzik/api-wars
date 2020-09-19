# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                 data format functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import locale
import constants as c


# -------------------------------------------------- main functions ---------------------------------------------------

def subject_format_data(subject: str, data: list) -> list:
    """ Returns formatted the subject data. """
    locale.setlocale(locale.LC_ALL, '')

    for item in data:
        if subject == c.SUBJECT.PLANETS:
            item[c.KEY.PLANETS.DIAMETER] = _format_diameter(item[c.KEY.PLANETS.DIAMETER])
            item[c.KEY.PLANETS.WATER] = _format_water(item[c.KEY.PLANETS.WATER])
            item[c.KEY.PLANETS.POPULATION] = _format_population(item[c.KEY.PLANETS.POPULATION])

    return data


# ------------------------------------------------- format functions --------------------------------------------------

def _format_diameter(data):
    return '{:n} km'.format(int(data)) if data != 'unknown' else data


def _format_water(data):
    if data == 'unknown':
        return data
    if data == '0':
        return 'no water'

    return f'{data}%'


def _format_population(data):
    return '{:n} people'.format(int(data)) if data != 'unknown' else data