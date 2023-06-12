#!/usr/bin/python3
"""
    Module for Rectangle class that imports from BaseGeometry
"""


BaseGeo = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeo):
    """
        Rectangle class

        Methods:
            __init__ - initializes object
            __str__ - str rep object
            area - return area of object
    """

    def __init__(self, width, height):
        """ initializes Rectangle object """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ return str rep of Rectangle object """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ returns area of Rectangle object """
        return (self.__width * self.__height)
