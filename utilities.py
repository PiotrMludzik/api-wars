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


def json_response(func):
    """ Converts the returned dictionary into a JSON response. """
    from functools import wraps
    from flask import jsonify

    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify(func(*args, **kwargs))

    return decorated_function
