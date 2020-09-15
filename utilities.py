# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      utilities
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------


def prepare_header_names(raw_names: str) -> list:
    """
        Returns the list of header names, where:
            * character '_' is replaced with a space ' ';
            * the first letter in a word is capitalized.
    """
    return [name.replace('_', ' ').capitalize() for name in raw_names]
