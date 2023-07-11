#!/usr/bin/python3

"""7-base_geometry.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """

    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """returns the rectangle area"""
        return (self.__height * self.__width)

    def __str__(self):
        """prints Rectangle"""
        output = '[' + str(self.__class__.__name__) + '] '
        output += str(self.__width) + '/' + str(self.__height)
        return (output)
