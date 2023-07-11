#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """
    reads a text file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        buffer = f.read()
        print(buffer)
