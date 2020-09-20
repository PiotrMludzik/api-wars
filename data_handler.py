# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                data handler functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import swapi


# --------------------------------------------------- data handlers ---------------------------------------------------

def data_get(subject: str, page_number: int) -> dict:
    """ Gets the subject data. """
    data = swapi.get_data(f'{subject}/?page={page_number}')

    # error handling
    if 'detail' in data and data['detail'] == 'Not found':
        raise ValueError(f'Page {page_number} with list of the {subject} not found.')

    return data


def data_prepare(subject: str, raw_data: dict) -> list:
    """ Returns only the necessary data for a given subject. """
    def needed_data_get(subject_name: str) -> list:
        if subject_name == c.SUBJECT.PLANETS:
            data_name = c.DATA.PLANETS
        elif subject_name == c.SUBJECT.STARSHIPS:
            data_name = c.DATA.STARSHIPS
        elif subject_name == c.SUBJECT.VEHICLES:
            data_name = c.DATA.VEHICLES
        elif subject_name == c.SUBJECT.PEOPLE:
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


def data_replace_links_with_data(data: list) -> list:
    """ Replaces links to data with the name of the data. """
    def replace_link_data(link: str) -> str:
        """ Returns a name of thing. """
        return swapi.get_data_name(link)

    def unpack_list_data(lst: list) -> str:
        """ Converts an items on a list to a string. """
        return ', '.join(lst)

    # ------------- data_replace_links_with_data() -------------
    for record in data:
        for key, value in record.items():
            if type(value) == list:
                for index in range(len(value)):
                    if swapi.has_api_url(value[index]):
                        value[index] = replace_link_data(value[index])

                record[key] = unpack_list_data(record[key])
            else:
                if swapi.has_api_url(value):
                    record[key] = replace_link_data(record[key])

    return data


# ------------------------------------------------ other data handlers ------------------------------------------------

def column_names_get(subject: str) -> list:
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


def page_pagination_number_get(items_number: int) -> int:
    """
        Calculates the number of pages of pagination.
        The result is rounded up from the formula:
        (numerator + denominator - 1) // denominator
    """
    return (items_number + swapi.PAGINATION_NUMBER - 1) // swapi.PAGINATION_NUMBER
