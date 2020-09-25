# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                     data handler: data processing and preparation
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


def data_prepare(subject: str, raw_data: list, modal_window: bool = False) -> list:
    """ Returns only the necessary data for a given subject. """
    headers_list = headers_get(subject, modal_window)
    prepared_data = []
    for raw_item in raw_data:
        prepared_item = {}
        for key in headers_list:
            prepared_item[key] = raw_item[key]
        prepared_data.append(prepared_item)

    return prepared_data


def headers_get(subject: str, modal_window: bool) -> tuple:
    """ Returns the necessary header names. """
    def headers_based_on_subject(subject_name: str) -> tuple:
        """ Collects header names. """
        if subject_name == dc.SUBJECT.PLANETS:
            header_names = dc.HEADERS.PLANETS
        elif subject_name == dc.SUBJECT.STARSHIPS:
            header_names = dc.HEADERS.STARSHIPS
        elif subject_name == dc.SUBJECT.VEHICLES:
            header_names = dc.HEADERS.VEHICLES
        elif subject_name == dc.SUBJECT.PEOPLE:
            header_names = dc.HEADERS.PEOPLE
        else:
            raise ValueError(f'The header names for {subject} not found.')

        return header_names

    def headers_for_modal_window(subject_name: str, header_names: tuple) -> tuple:
        """ Removes headings that contain buttons. """
        if subject_name == dc.SUBJECT.PLANETS:
            headers_with_button = dc.COLUMN_WITH_BUTTON.PLANETS
        elif subject_name == dc.SUBJECT.STARSHIPS:
            headers_with_button = dc.COLUMN_WITH_BUTTON.STARSHIPS
        elif subject_name == dc.SUBJECT.VEHICLES:
            headers_with_button = dc.COLUMN_WITH_BUTTON.VEHICLES
        elif subject_name == dc.SUBJECT.PEOPLE:
            headers_with_button = dc.COLUMN_WITH_BUTTON.PEOPLE
        else:
            raise ValueError(f'The columns that contain buttons for {subject} not found.')

        header_names = list(header_names)
        for header_to_remove in headers_with_button:
            header_names.remove(header_to_remove)

        return tuple(header_names)

    # ------------- headers_get() -------------
    headers = headers_based_on_subject(subject)
    if modal_window:
        headers = headers_for_modal_window(subject, headers)

    return headers


def display_name(subject_data: list, column_name: str) -> list:
    """ Display name instead of url (only on buttons). """
    for record in subject_data:
        url = "".join(record[column_name])
        record[column_name] = swapi.get_data_name(url, full_url=True)

    return subject_data


# -------------------------------------------------- button handlers --------------------------------------------------

def button_data_headers_get(subject: str) -> tuple:
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
        raise ValueError(f'There are no column names for the button data in the {subject} subject.')


def button_data_get_data(subject_data: tuple, column_names: tuple) -> list:
    """ Returns the data list for the corresponding column for button insertion. """
    def unpack_data(data: list) -> str:
        """ Returns a string concatenated with the list data. """
        return ', '.join(data)

    # ------------- button_data_get_data() -------------
    button_data = []
    for record in subject_data:
        record_data = {}
        for key in column_names:
            data = record[key]
            record_data[key] = {
                'amount of data': len(data),
                'data': unpack_data(data)
            }

        button_data.append(record_data)

    return button_data


# --------------------------------------------------- api handlers ----------------------------------------------------

def api_data_get(request_data: list) -> list:
    """ Prepares data at the client's request. """
    response_data = []
    for url in request_data:
        response_data.append(swapi.get_data(url, full_url=True))

    return response_data


def subject_get_proper(subject: str) -> str:
    """ Returns proper subject. """
    if subject in dc.COLUMN_NAMES_WITH_PLANETS:
        subject = dc.SUBJECT.PLANETS
    elif subject in dc.COLUMN_NAMES_WITH_PEOPLE:
        subject = dc.SUBJECT.PEOPLE

    return subject


# ------------------------------------------------ other data handlers ------------------------------------------------

def column_names_get(subject: str) -> tuple:
    """ Returns column names. """
    if subject == dc.SUBJECT.PLANETS:
        return dc.HEADERS.PLANETS
    elif subject == dc.SUBJECT.STARSHIPS:
        return dc.HEADERS.STARSHIPS
    elif subject == dc.SUBJECT.VEHICLES:
        return dc.HEADERS.VEHICLES
    elif subject == dc.SUBJECT.PEOPLE:
        return dc.HEADERS.PEOPLE
    else:
        raise ValueError(f'There are no column names for the {subject} subject.')


def column_names_prepare(raw_names: tuple) -> tuple:
    """
        Returns the tuple of column names, where:
            * character '_' is replaced with a space ' ';
            * the first letter in a word is capitalized.
    """
    return tuple([name.replace('_', ' ').capitalize() for name in raw_names])


def page_pagination_number_get(items_number: int) -> int:
    """
        Calculates the number of pages of pagination.
        The result is rounded up from the formula:
        (numerator + denominator - 1) // denominator
    """
    return (items_number + swapi.PAGINATION_NUMBER - 1) // swapi.PAGINATION_NUMBER
