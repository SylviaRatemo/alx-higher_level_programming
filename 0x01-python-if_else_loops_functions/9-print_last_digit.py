#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    rem = number % 10
    if rem == 0:
        print(0)
    else:
        print(rem)
