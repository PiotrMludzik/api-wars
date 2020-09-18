# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import data_handler as dh
import session
import utilities as util


def subject_get_data(subject: str, page_number: int) -> list:
    """ Collects the subject data. """
    data = dh.subject_get_data(subject, page_number)
    pagination_number_set(subject, data['count'])  # 'count' - the number of items in subject
    data = dh.subject_prepare_data(subject, data['results'])  # 'results' - the subject data
    data = dh.subject_format_data(subject, data)

    return data


def subjects_get_list() -> list:
    """ Returns a subjects name list. """
    return dh.subjects_get_list()


def columns_name_get(subject) -> list:
    """ Returns columns name. """
    if subject == c.SUBJECT.PLANETS:
        return util.prepare_header_names(c.DATA.PLANETS)
    elif subject == c.SUBJECT.STARSHIPS:
        return util.prepare_header_names(c.DATA.STARSHIPS)
    elif subject == c.SUBJECT.VEHICLES:
        return util.prepare_header_names(c.DATA.VEHICLES)
    else:
        raise ValueError(f'There are no column names for the {subject} subject.')


def pagination_number_set(page_name, items_number):
    """ Sets the number of subpages (pagination of the page) and remembers it as variable in the sessions. """
    pagination_number = dh.get_page_pagination_number(items_number)
    session.set_pagination_number(page_name, pagination_number)


def pagination_number_get(page_name) -> int:
    return session.get_pagination_number(page_name)
