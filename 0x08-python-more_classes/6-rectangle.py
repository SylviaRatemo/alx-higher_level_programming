#!/usr/bin/python3
"""A class description of a rectangle based on 5-rectangle."""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialization function
        Attributes:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Height getter function
        Returns:
            rectangle height
        """
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

    def area(self):
        """Function to compute area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Functio to compute perimeter of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Function to print rectangle with #"""

        rect = ""
        if self.__height == 0 or self.__width == 0:
            return rect
        for i in range(self.__height):
            rect += ("#" * self.__width)
            if i != self.__height - 1:
                rect += "\n"
        return(rect)

    def __repr__(self):
        """Function to return string representation of rectangle"""
        h = str('self.height')
        w = str('self.width')
        return "Rectangle({}, {})".format(eval(h), eval(w))

    def __del__(self):
        """Function to print message on deletion of class instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
