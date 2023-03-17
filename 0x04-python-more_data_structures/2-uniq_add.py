#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    total = 0
    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)
    for k in uniq_list:
        total += k
    return total
