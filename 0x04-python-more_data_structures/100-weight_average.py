#!/usr/bin/python3
def weighted_average(my_list=[]):
    numerator = 0
    if my_list == NULL:
        return 0
    for x in my_list:
        for y in my_list:
            numerator += (x * y)
            y += y
    return numerator / y
