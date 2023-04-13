#!/usr/bin/python3
"""Class student"""


class Student:
    """Class student descriptio"""

    def __init__(self, first_name="", last_name="", age=0):
        """Class constructor
        Attributes:
            first_name (str): First name
            last_name (str): Last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary of student
        Attributes:
            attrs (list): attributes to be printed
        """
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
