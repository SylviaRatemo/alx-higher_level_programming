#!/usr/bin/python3
""""First class Base"""
import json


class Base:
    """"Class Base Description"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON sring"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
