#!/usr/bin/python3
"""Function to write object to text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function definition"""

    text = json.dumps(my_obj)
    with open(filename, mode="w") as myFile:
        return myFile.write(text)
