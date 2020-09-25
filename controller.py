# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import data_handler as dh
import data_format as df
import session
import utilities as util


# ------------------------------------------------- data controllers --------------------------------------------------

def data_get(subject: str, page_number: int) -> tuple:
    """ Collects the subject data. """
    data = dh.data_get(subject, page_number)
    pagination_number_set(subject, data['count'])  # 'count' - the number of items in subject
    data = dh.data_prepare(subject, data['results'])  # 'results' - the subject data
    data = df.data_format(subject, data)

    return tuple(data)


# ------------------------------------------------ button controllers -------------------------------------------------

def button_data_get(subject: str, subject_data: tuple) -> list:
    """ Returns the button data needed to handle client-side events. """
    def unpack_data(data: list) -> str:
        """ Returns a string concatenated with the list data. """
        return ', '.join(data)

    needed_columns = dh.button_data_get_needed_columns(subject)

    record_data = []
    for record in subject_data:
        button_data = {}
        for column_name in needed_columns:
            button_data[column_name] = {
                'amount of data': len(record[column_name]),
                'data': unpack_data(record[column_name])
            }

        record_data.append(button_data)

    return record_data


# -------------------------------------------------- api controllers --------------------------------------------------

def api_data_get(request_data: dict) -> dict:
    """
        Prepares data at the client's request.

        Valid request pattern:
        {
            'api_wars':
                {
                    'swapi':
                        {
                            'request': [ <list of the url requests to the swapi api database> ]
                        },
                }
        }

        Valid response pattern:
        {
            'api_wars':
                {
                    'swapi':
                        {
                            'response': [ <list of the url response from the swapi api database> ]
                        },
                    'modal window':
                        {
                            'injection code': ' <html string with data for injection to modal window> '
                        }
                }
        }
    """
    if not request_data:
        return {'valueError': 'None request data.'}
    if c.API_KEY.HEADER not in request_data:
        return {'valueError': 'Wrong request data.'}

    SWAPI_REQUEST = request_data[c.API_KEY.HEADER][c.API_KEY.SWAPI][c.API_KEY.REQUEST]

    return {
        c.API_KEY.HEADER: {
            c.API_KEY.SWAPI: {
                c.API_KEY.RESPONSE: dh.api_data_get(SWAPI_REQUEST)
            }
        }
    }


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
