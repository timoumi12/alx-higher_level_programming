#!/usr/bin/python3
"""models/base.py"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
