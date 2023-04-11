#!/usr/bin/python3
"""Class than inherits from list"""


class MyList(list):
    """Class definition for MyList"""

    def print_sorted(self):
        return (sorted(list(self))
