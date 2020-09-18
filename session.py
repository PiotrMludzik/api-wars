# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                    session handler
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

from flask import session


def set_pagination_number(page_name: str, pagination_number: int):
    """ Sets the pagination number variable to session. """
    session[f'pagination_{page_name}'] = pagination_number


def get_pagination_number(page_name: str) -> int:
    """ Gets the pagination number from variable in session. """
    return session[f'pagination_{page_name}']
