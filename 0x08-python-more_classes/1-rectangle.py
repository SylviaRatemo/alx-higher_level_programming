#!/usr/bin/python3
"""A class description of a rectangle based on 0-rectangle."""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization function
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """Height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter function.
        Attributes:
            height (int): height of the rectangle
        Raises:
            ValueError: If height < 0
            TypeError: If height is not an int
        """
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Width getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter Function.
        Attributes:
            width (int): the width of the rectangle
        Raises:
            ValueError: If width is < 0
            TypeError: If width is not an int
        """

        if not isinstance(value, int):
            raise TypeError("width must be an int")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
