# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                 data format functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import locale
import constants as c
import utilities as util


# -------------------------------------------------- main functions ---------------------------------------------------

def subject_format_data(subject: str, data: list) -> list:
    """ Returns formatted the subject data. """
    locale.setlocale(locale.LC_ALL, '')

    for item in data:
        if subject == c.SUBJECT.PLANETS:
            item[c.KEY.PLANETS.DIAMETER] = _format_diameter(item[c.KEY.PLANETS.DIAMETER])
            item[c.KEY.PLANETS.WATER] = _format_water(item[c.KEY.PLANETS.WATER])
            item[c.KEY.PLANETS.POPULATION] = _format_population(item[c.KEY.PLANETS.POPULATION])
        elif subject == c.SUBJECT.STARSHIPS:
            item[c.KEY.STARSHIPS.CREW] = _format_crew_and_passengers(item[c.KEY.STARSHIPS.CREW])
            item[c.KEY.STARSHIPS.PASSENGERS] = _format_crew_and_passengers(item[c.KEY.STARSHIPS.PASSENGERS])
            item[c.KEY.STARSHIPS.CARGO] = _format_cargo(item[c.KEY.STARSHIPS.CARGO])
            item[c.KEY.STARSHIPS.LENGTH] = _format_length(item[c.KEY.STARSHIPS.LENGTH])
            item[c.KEY.STARSHIPS.ATSP] = _format_atsp(item[c.KEY.STARSHIPS.ATSP])
            item[c.KEY.STARSHIPS.MGLT] = _format_mglt(item[c.KEY.STARSHIPS.MGLT])
    return data


def column_names_format(column_names: list) -> list:
    """ Return a formatted column name if necessary. """
    MGlT = c.KEY.STARSHIPS.MGLT
    if MGlT in column_names:
        column_names = util.change_list_value(column_names, MGlT, c.NEW_COLUMN_NAME.MGLT)

    return column_names


# ------------------------------------------------- format functions --------------------------------------------------

def _format_diameter(data: str) -> str:
    return '{:n} km'.format(int(data)) if data != 'unknown' else data


def _format_water(data: str) -> str:
    if data == 'unknown':
        return data
    if data == '0':
        return 'no water'

    return f'{data}%'


def _format_population(data: str) -> str:
    return '{:n} people'.format(int(data)) if data != 'unknown' else data


def _format_crew_and_passengers(data: str) -> str:
    data = data.replace(",", "")  # for numbers with the thousand separator

    if data == 'unknown':
        return data
    if data == 'n/a':
        return 'not available'
    if data == '0':
        return 'does not carry'
    if data == '1':
        return f'{data} person'
    if data.isdigit():
        return '{:n} people'.format(int(data))

    return f'{data} people'


def _format_cargo(data: str) -> str:
    return '{:n} kg'.format(int(data)) if data != 'unknown' else data


def _format_length(data: str) -> str:
    data = data.replace(",", ".")  # for numbers with the "," thousand separator

    return '{:n} m'.format(float(data)) if data != 'unknown' else data


def _format_atsp(data: str) -> str:
    if data == 'n/a':
        return 'not available'

    return '{:n} km/h'.format(float(data)) if data != 'unknown' else data


def _format_mglt(data: str) -> str:
    return '{:n} mglt/h'.format(float(data)) if data != 'unknown' else data
