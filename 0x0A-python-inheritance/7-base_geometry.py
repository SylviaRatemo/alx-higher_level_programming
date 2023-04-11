#!/usr/bin/python3
"""class BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """Class definition"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if   type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
