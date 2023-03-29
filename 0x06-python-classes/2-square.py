#!/usr/bin/python3
"""Define a class based on 1-square.py."""


class Square:
    """Representation of the square."""

    def __init__(self, size=0):
        """Initialization function.
        Attributes:
            size (int): size of the square.
        Raises:
            ValueError: If size < 0.
            TypeError: If size is not an int.
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
