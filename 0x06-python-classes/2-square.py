#!/usr/bin/python3

"""Defines Square class"""


class Square:
    """creates a square"""
    def __init__(self, size=0):
        """ Initializes a new square

        Args:
        size (int): the size of new square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
