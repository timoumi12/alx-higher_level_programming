#!/usr/bin/python3

"""Defines Square class"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        """ Initializes a new square

        Args:
        size (int): the size of new square
        """
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the square area"""
        return (self.__size**2)
