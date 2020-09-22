# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      utilities
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------


def change_list_value(array: list, value_old: str, value_new: str) -> list:
    """ Returns a given list with a changed value. """
    for index, value in enumerate(array):
        if value == value_old:
            array[index] = value_new

    return array
