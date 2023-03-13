#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list) - 1):
        if mylist[i].isdigit():
            print("{}".format(my_list[i]))
            print()
