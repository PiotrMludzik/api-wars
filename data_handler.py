# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                data handler functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import data_constants as dc
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
        if subject_name == dc.SUBJECT.PLANETS:
            data_name = dc.DATA.PLANETS
        elif subject_name == dc.SUBJECT.STARSHIPS:
            data_name = dc.DATA.STARSHIPS
        elif subject_name == dc.SUBJECT.VEHICLES:
            data_name = dc.DATA.VEHICLES
        elif subject_name == dc.SUBJECT.PEOPLE:
            data_name = dc.DATA.PEOPLE
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


# -------------------------------------------------- button handlers --------------------------------------------------

def button_data_get_names(subject: str) -> tuple:
    """ Returns the names of data for the corresponding column for button insertion. """
    if subject == dc.SUBJECT.PLANETS:
        return dc.COLUMN_WITH_BUTTON.PLANETS
    elif subject == dc.SUBJECT.STARSHIPS:
        return dc.COLUMN_WITH_BUTTON.STARSHIPS
    elif subject == dc.SUBJECT.VEHICLES:
        return dc.COLUMN_WITH_BUTTON.VEHICLES
    elif subject == dc.SUBJECT.PEOPLE:
        return dc.COLUMN_WITH_BUTTON.PEOPLE
    else:
        raise ValueError(f'There are no names for the button data in the {subject} subject.')


def button_data_get_data(subject_data: list, column_names: tuple) -> tuple:
    """ Returns the data tuple for the corresponding column for button insertion. """
    button_data = []
    for record in subject_data:
        record_data = {}
        for key in column_names:
            record_data[key] = (record[key])

        button_data.append(record_data)

    return tuple(button_data)


# ------------------------------------------------ other data handlers ------------------------------------------------

def column_names_get(subject: str) -> list:
    """ Returns column names. """
    if subject == dc.SUBJECT.PLANETS:
        return dc.DATA.PLANETS.copy()
    elif subject == dc.SUBJECT.STARSHIPS:
        return dc.DATA.STARSHIPS.copy()
    elif subject == dc.SUBJECT.VEHICLES:
        return dc.DATA.VEHICLES.copy()
    elif subject == dc.SUBJECT.PEOPLE:
        return dc.DATA.PEOPLE.copy()
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
