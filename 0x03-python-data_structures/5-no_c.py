#!/usr/bin/python3
def no_c(my_string):
    reps = [('c', ''), ('C', '')]
    for char, rep in reps:
        if char in my_string:
            my_string = my_string.replace(char, rep)

    print(my_string)
