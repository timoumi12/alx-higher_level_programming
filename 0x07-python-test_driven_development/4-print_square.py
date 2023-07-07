#!/usr/bin/python3

"""
    4-print_square function

    creates a function that adds two integers
"""


def print_square(size):
    """prints a square while checking edge cases"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for rows in range(size):
        for cols in range(size):
            print('#', end='')
        print()
