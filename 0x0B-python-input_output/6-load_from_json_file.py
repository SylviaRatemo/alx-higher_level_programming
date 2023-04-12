#!/usr/bin/python3
"""Function to create object from JSON file"""
import json


def load_from_json_file(filename):
    """Function definition"""

    with open(filename, mode="r", encoding="utf-8") as myFile:
        code = myFile.read()
    return json.loads(code)
