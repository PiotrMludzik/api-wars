# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import data_handler as dh
import data_format as df
import session


def subject_get_data(subject: str, page_number: int) -> list:
    """ Collects the subject data. """
    data = dh.subject_get_data(subject, page_number)
    pagination_number_set(subject, data['count'])  # 'count' - the number of items in subject
    data = dh.subject_prepare_data(subject, data['results'])  # 'results' - the subject data
    data = df.subject_format_data(subject, data)

    return data


def subjects_get_list() -> list:
    """ Returns a subject names list. """
    return dh.subjects_get_list()


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
