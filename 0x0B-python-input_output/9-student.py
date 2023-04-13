#!/usr/bin/python3
"""Class student"""


class Student:
    """Class student descriptio"""


    def __init__(self, first_name, last_name, age):
        """Class constructor
        Attributes:
            first_name (str): First name
            last_name (str): Last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary of student"""
        return self.__dict__
