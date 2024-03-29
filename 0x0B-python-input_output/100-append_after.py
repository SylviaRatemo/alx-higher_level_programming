#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Function definition"""
    text = ""
    with open(filename, "r") as myFile:
        for line in myFile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file:
        file.write(text)
