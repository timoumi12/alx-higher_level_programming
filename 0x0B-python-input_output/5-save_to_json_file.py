#!/usr/bin/python3
import json
"""4-from_json_string.py"""


def save_to_json_file(my_obj, filename):
    """
    deserializes an object
    """
    with open(filename, 'w') as f:
        json.dumps(my_obj, f)
