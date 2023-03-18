#!/usr/bin/python3
def weight_average(my_list=[]):
    denom = 0
    prod = 0
    if len(my_list) == 0:
        return 0
    for x in my_list:
        prod += x[0] * x[1]
        denom += x[1]
    return prod / denom
