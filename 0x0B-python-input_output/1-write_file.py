#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """
    writes to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
