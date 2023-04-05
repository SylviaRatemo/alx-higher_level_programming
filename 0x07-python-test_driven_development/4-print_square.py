#!/usr/bin/python3
"""Print Square module"""


def print_square(size):
    """Function that prints perfect square
    Attributes:
        size (int, float): size of square
    Raises:
        TypeError: size not an int
        ValueError: size < 0
    """

    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))
