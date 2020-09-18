# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import data_handler as dh
import session
import utilities as util


def planets_get_data(page_number: int) -> list:
    """ Collects the planets' data. """
    planets_data = dh.planets_get_data(page_number)
    pagination_number_set('planets', planets_data['count'])  # 'count' - the number of planets
    planets_data = dh.planets_prepare_data(planets_data['results'])  # 'results' - the planets data
    planets_data = dh.planets_format_data(planets_data)

    return planets_data


def columns_name_get() -> list:
    """ Returns columns name """
    return util.prepare_header_names(c.PLANETS_COLUMN_ORDER)


def pagination_number_set(page_name, items_number):
    """ Sets the number of subpages (pagination of the page) and remembers it as variable in the sessions """
    pagination_number = dh.get_page_pagination_number(items_number)
    session.set_pagination_number(page_name, pagination_number)


def pagination_number_get(page_name) -> int:
    return session.get_pagination_number(page_name)
