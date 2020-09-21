# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import data_handler as dh
import data_format as df
import session


def data_get(subject: str, page_number: int) -> list:
    """ Collects the subject data. """
    data = dh.data_get(subject, page_number)
    pagination_number_set(subject, data['count'])  # 'count' - the number of items in subject
    data = dh.data_prepare(subject, data['results'])  # 'results' - the subject data
    data = df.data_format(subject, data)

    return data


def button_data_get(subject, subject_data: list) -> tuple:
    """ Returns the button data (a tuple names and a dictionary of the data) for the proper column. """
    btn_name = dh.button_data_get_names(subject)
    btn_data = dh.button_data_get_data(subject_data, btn_name)

    return btn_name, btn_data


def column_names_get(subject) -> list:
    """ Returns column names. """
    column_names = dh.column_names_get(subject)
    column_names = df.column_names_format(column_names)
    column_names = dh.column_names_prepare(column_names)

    return column_names


def pagination_number_set(page_name, items_number):
    """ Sets the number of subpages (pagination of the page) and remembers it as variable in the sessions. """
    pagination_number = dh.page_pagination_number_get(items_number)
    session.pagination_number_set(page_name, pagination_number)


def pagination_number_get(page_name) -> int:
    """ Gets the pagination number from variable in session. """
    return session.pagination_number_get(page_name)
