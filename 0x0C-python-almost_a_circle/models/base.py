#!/usr/bin/python3
"""models/base.py"""
import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
