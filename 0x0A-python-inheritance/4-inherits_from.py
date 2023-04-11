#!/usr/bin/python3
"""Function to check inheritance"""


def inherits_from(obj, a_class):
    """Function definition for inheritance"""

    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
