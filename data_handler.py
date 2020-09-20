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
    def needed_data_get(data_name: str) -> list:
        if subject == c.SUBJECT.PLANETS:
            data_name = c.DATA.PLANETS
        elif subject == c.SUBJECT.STARSHIPS:
            data_name = c.DATA.STARSHIPS
        elif subject == c.SUBJECT.VEHICLES:
            data_name = c.DATA.VEHICLES
        elif subject == c.SUBJECT.PEOPLE:
            data_name = c.DATA.PEOPLE
        else:
            raise ValueError(f'Needed data for {subject} not found.')

        return data_name

    # ------------- subject_prepare_data() -------------
    needed_data = needed_data_get(subject)
    prepared_data = []
    for raw_item in raw_data:
        prepared_item = {}
        for key in needed_data:
            prepared_item[key] = raw_item[key]
        prepared_data.append(prepared_item)

    return prepared_data


def subjects_get_list() -> list:
    """ Returns a subject names list. """
    attributes_list = [a for a in dir(c.SUBJECT) if not a.startswith('__')]
    values_list = []
    for attribute in attributes_list:
        values_list.append(getattr(c.SUBJECT, attribute))

    return values_list


# ------------------------------------------------ other data handlers ------------------------------------------------

def column_names_get(subject) -> list:
    """ Returns column names. """
    if subject == c.SUBJECT.PLANETS:
        return c.DATA.PLANETS.copy()
    elif subject == c.SUBJECT.STARSHIPS:
        return c.DATA.STARSHIPS.copy()
    elif subject == c.SUBJECT.VEHICLES:
        return c.DATA.VEHICLES.copy()
    elif subject == c.SUBJECT.PEOPLE:
        return c.DATA.PEOPLE.copy()
    else:
        raise ValueError(f'There are no column names for the {subject} subject.')


def column_names_prepare(raw_names: list) -> list:
    """
        Returns the list of column names, where:
            * character '_' is replaced with a space ' ';
            * the first letter in a word is capitalized.
    """
    return [name.replace('_', ' ').capitalize() for name in raw_names]


def page_pagination_number_get(items_number):
    """
        Calculates the number of pages of pagination.
        The result is rounded up from the formula:
        (numerator + denominator - 1) // denominator
    """
    return (items_number + swapi.PAGINATION_NUMBER - 1) // swapi.PAGINATION_NUMBER
