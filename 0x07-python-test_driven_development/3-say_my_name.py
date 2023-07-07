#!/usr/bin/python3

"""
    3-say_my_name function

    creates a function that adds two integers
"""


def say_my_name(first_name, last_name=""):
    """prints my names is 'Fname' 'Lname' while checking edge cases"""

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    else:
        print('My name is {} {}'.format(first_name, last_name))
