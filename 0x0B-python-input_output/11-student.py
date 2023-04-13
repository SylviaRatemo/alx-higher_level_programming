#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Definition a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Attributes:
            first_name (str): First name
            last_name (str): Last name
            age (int): Student's Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        Args:
            attrs (list): The attributes to be printed.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
