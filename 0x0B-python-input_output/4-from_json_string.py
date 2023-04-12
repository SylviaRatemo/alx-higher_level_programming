#!/usr/bin/python3
"""Return object represented by JSON string"""
import json


def from_json_string(my_str):
    """Function definition"""

    return json.loads(my_str)
