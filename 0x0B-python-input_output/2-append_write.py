#!/usr/bin/python3
"""1-write_file.py"""


def append_write(filename="", text=""):
    """
    writes to a text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
