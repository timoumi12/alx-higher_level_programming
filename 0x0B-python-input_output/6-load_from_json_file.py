#!/usr/bin/python3
import json
"""6-load_from_json_file.py"""


def load_from_json_file(filename):
    """
    Create object from a JSON file
    """
    with open(filename, 'r') as f:
        return json.load(f)
