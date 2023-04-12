#!/usr/bin/python3
"""Function to append string at the end of text file(UTF8)"""


def append_write(filename="", text=""):
    """Function definition"""

    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
