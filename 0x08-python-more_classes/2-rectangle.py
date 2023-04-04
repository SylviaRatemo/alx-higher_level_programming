#!/usr/bin/python3
"""A class description of a rectangle based on 1-rectangle"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function.
        Attributes:
            width (int): width of the rectangle
        Raises:
            ValueError: If width < 0
            TypeError: If width is not an int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter Function.
        Attributes:
            height (int): the height of the rectangle
        Raises:
            ValueError: If height is < 0
            TypeError: If height is not an int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__weight

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
