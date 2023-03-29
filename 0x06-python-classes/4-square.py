#!/usr/bin/python3
"""Define a class based on 3-square.py."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialization function.
        Attributes:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gettor function.
        Returns:
            The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Settor function.
        Attributes:
            size (int): size of the square
        Raises:
            ValueError: If size < 0
            TypeError: If size is not an int
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public function compute area.
        Returns:
            The current square area
        """
        return (self.__size * self.__size)
