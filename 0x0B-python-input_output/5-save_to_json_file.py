#!/usr/bin/python3
"""4-from_json_string.py"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
