#!/usr/bin/python3
"""models/square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""


    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size"""
        return self.height

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns the print() and str() representation of the Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                       self.x, self.y,
                                                       self.width)
