#!/usr/bin/python3

"""Defines Rectangle Class"""


class Rectangle:
    """Creates a Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of a new Reactangle

        Args:
        width (int): the width of new Rectangle
        height (int): the height of new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints Rectangle"""
        output = ""
        if self.__width == 0 or self.__height == 0:
            return (output)
        for i in range(self.__height - 1):
            output += "#" * self.__width + '\n'
        output += "#" * self.__width
        return (output)
