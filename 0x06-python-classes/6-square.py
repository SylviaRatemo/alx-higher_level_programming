#!/usr/bin/python3
"""Define a class based on 5-square.py."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization function.
        Attributes:
            size (int): size of the square
            position (tuple): tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Position settor function."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Position gettor function."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public function compute area.
        Returns:
            The current square area
        """
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """Funtion to print in stdout the square with #."""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
