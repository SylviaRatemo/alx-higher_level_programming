#!/usr/bin/python3
"""Function to read text file (UTF8)"""


def read_file(filename=""):
    """Function definition"""

    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read())
