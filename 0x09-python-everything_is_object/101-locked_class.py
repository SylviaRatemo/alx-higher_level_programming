#!/usr/bin/python3
"""Definitiona of a locked class."""


class LockedClass:
    """A class that prevents the creation of a attribute instances not named first_name"""

    __slots__ = ["first_name"]
