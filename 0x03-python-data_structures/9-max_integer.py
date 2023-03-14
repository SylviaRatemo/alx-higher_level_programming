#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    count = len(my_list) - 1
    while count > 0:
        j = 0
        while j < count:
            if my_list[j] < my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        count -= 1
    return (my_list[0]))
