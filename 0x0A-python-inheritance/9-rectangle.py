#!/usr/bin/python3
"""class BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """Class definition"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class Rectangle inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class definition"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] <width>/<height>"
    
    def __print__(self):
        print(sel.__str__)
