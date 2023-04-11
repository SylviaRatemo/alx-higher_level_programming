#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class Rectangle inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class Definition"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
