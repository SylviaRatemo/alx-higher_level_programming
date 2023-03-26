#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        val = ord(char)
        if val >= 97 and val <= 122:
            val -= 32
        new_str += chr(val)
    print(new_str)
