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
        elif subject == c.SUBJECT.STARSHIPS:
            needed_data = c.DATA.STARSHIPS
        elif subject == c.SUBJECT.VEHICLES:
            needed_data = c.DATA.VEHICLES
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


def subjects_get_list() -> list:
    """ Returns a subject names list. """
    attributes_list = [a for a in dir(c.SUBJECT) if not a.startswith('__')]
    values_list = []
    for attribute in attributes_list:
        values_list.append(getattr(c.SUBJECT, attribute))

    return values_list


# ------------------------------------------------ other data handlers ------------------------------------------------

def page_pagination_number_get(items_number):
    """
        Calculates the number of pages of pagination.
        The result is rounded up from the formula:
        (numerator + denominator - 1) // denominator
    """
    return (items_number + swapi.PAGINATION_NUMBER - 1) // swapi.PAGINATION_NUMBER
