#!/usr/bin/python3
"""Function to return description with simple data structure"""
import json


def class_to_json(obj):
    """Function definition"""

    return obj.__dict__
