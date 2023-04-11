#!/usr/bin/python3
"""Function to check object instance"""


def is_kind_of_class(obj, a_class):
    """Function definition"""

    if type(obj) is a_class:
        return True
    return False
