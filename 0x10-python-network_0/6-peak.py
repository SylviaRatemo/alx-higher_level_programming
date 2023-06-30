#!/usr/bin/python3
"""Find the peak"""
def find_peak(list_of_integers):
    COUNT = 0
    HIGH = 0
    for i in list_of_integers:
        if i > HIGH:
            HIGH = i
            COUNT += 1
    if COUNT < 1:
        return None
    return HIGH
