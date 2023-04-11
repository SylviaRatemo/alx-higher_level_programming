#!/usr/bin/python3
"""Function to check inheritance"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
