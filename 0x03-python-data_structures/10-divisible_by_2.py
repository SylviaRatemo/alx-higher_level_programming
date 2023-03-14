#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    limit = range(len(my_list))
    check = [True if my_list[x] % 2 == 0 else False for x in limit]
    return(check)
