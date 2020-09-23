# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import data_handler as dh
import data_format as df
import session


# ------------------------------------------------- data controllers --------------------------------------------------

def data_get(subject: str, page_number: int) -> tuple:
    """ Collects the subject data. """
    data = dh.data_get(subject, page_number)
    pagination_number_set(subject, data['count'])  # 'count' - the number of items in subject
    data = dh.data_prepare(subject, data['results'])  # 'results' - the subject data
    data = df.data_format(subject, data)

    return tuple(data)


# ------------------------------------------------ button controllers -------------------------------------------------

def button_data_get(subject: str, subject_data: tuple) -> dict:
    """ Returns the button data needed to handle client-side events. """
    column_names = dh.button_data_get_column_names(subject)
    data = dh.button_data_get_data(subject_data, column_names)

    return {'column name': column_names, 'data': data}


# -------------------------------------------------- api controllers --------------------------------------------------

def api_data_get(request_data: dict) -> dict:
    """ Prepares data at the client's request. """
    API_WARS = 'api_wars'
    if not request_data or API_WARS not in request_data:
        return {'valueError': 'None or wrong request data.'}

    return {API_WARS: dh.api_data_get(request_data[API_WARS])}


# ------------------------------------------------- other controllers -------------------------------------------------

def column_names_get(subject: str) -> tuple:
    """ Returns column names. """
    column_names = dh.column_names_get(subject)
    column_names = df.column_names_format(column_names)
    column_names = dh.column_names_prepare(column_names)

    return column_names


def pagination_number_set(page_name: str, items_number: int):
    """ Sets the number of subpages (pagination of the page) and remembers it as variable in the sessions. """
    pagination_number = dh.page_pagination_number_get(items_number)
    session.pagination_number_set(page_name, pagination_number)


def pagination_number_get(page_name: str) -> int:
    """ Gets the pagination number from variable in session. """
    return session.pagination_number_get(page_name)
