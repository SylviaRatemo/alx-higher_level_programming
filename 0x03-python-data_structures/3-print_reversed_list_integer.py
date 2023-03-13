#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
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
    for k in my_list:
        print(k)
