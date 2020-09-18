# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import constants as c
import data_handler as dh
import utilities as util


def planets_get_data(page_number: int) -> list:
    """ Collects the planets' data. """
    planets_data = dh.planets_get_data(page_number)
    planets_data = dh.planets_prepare_data(planets_data)
    planets_data = dh.planets_format_data(planets_data)

    return planets_data


def get_columns_name() -> list:
    """ Returns columns name """
    return util.prepare_header_names(c.PLANETS_COLUMN_ORDER)