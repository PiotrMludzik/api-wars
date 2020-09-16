# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                controller functions
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

import data_handler as dh


def planets_get_data(page_number: int = 1) -> list:
    """ Collects the planets' data. """
    planets_data = dh.planets_get_data(page_number)
    planets_data = dh.planets_prepare_data(planets_data)
    planets_data = dh.planets_format_data(planets_data)

    return planets_data
