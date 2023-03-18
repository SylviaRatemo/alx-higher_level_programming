#!/usr/bin/python3
def islower(c):
    val = ord(c)
    if val >= 97 and val <= 122:
        return True
    elif val >= 65 and val <= 90:
        return False
