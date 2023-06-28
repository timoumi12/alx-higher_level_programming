#!/usr/bin/python3

"""Defines Square class"""


class Square:
    """creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new square

        Args:
        size (int): the size of new square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """returns the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the position"""
        self.__position = value
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
