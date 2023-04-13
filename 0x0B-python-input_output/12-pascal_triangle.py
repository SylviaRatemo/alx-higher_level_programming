#!/usr/bin/python3
"""Function to print Pascal's Triangle."""


def pascal_triangle(n):
    """Definition of Pascal's Triangle
    Returns: int representation of Pascal Triangle
    """
    if n <= 0:
        return []

    pyramid = [[1]]
    while len(pyramid) != n:
        tri = pyramid[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        pyramid.append(tmp)
    return pyramid
