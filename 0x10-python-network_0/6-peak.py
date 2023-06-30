#!/usr/bin/python3
"""Find the peak"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""

    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return peak_recurse(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def peak_recurse(LO, start, stop):
    """Recursively finds peak"""
    if stop - start < 2:
        return None
    mid = (start + stop) // 2
    if LO[mid] >= LO[mid - 1] and LO[mid] >= LO[mid + 1]:
        return LO[mid]
    return peak_recurse(LO, start, mid) or peak_recurse(LO, mid, stop)
