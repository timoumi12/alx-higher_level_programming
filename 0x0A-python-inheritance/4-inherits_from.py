#!/usr/bin/python3

"""inherits_from function"""


def inherits_from(obj, a_class):
    """return True or False"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
