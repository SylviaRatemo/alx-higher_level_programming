#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i of x in my_list:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        print("")
        return (i)
