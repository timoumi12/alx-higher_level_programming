#!/usr/bin/python3

"""is_same_class function"""


def is_same_class(obj, a_class):
    """
    checks if 'obj' is an instance of 'a_class'
    """
    if issubclass(a_class, type(obj)):
        return (True)
    return (False)
