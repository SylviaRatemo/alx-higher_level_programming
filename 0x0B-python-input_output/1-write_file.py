#!/usr/bin/python3
"""Write string to text file(UTF8)"""


def write_file(filename="", text=""):
    """Function definition"""

    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
