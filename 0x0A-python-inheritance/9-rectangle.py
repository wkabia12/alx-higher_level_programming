#!/usr/bin/python3
"""
    Module for Rectangle class that imports from BaseGeometry
"""


BaseGeo = __import__('7-base_geometry.py').BaseGeometry


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
        super().integer_validation("width", width)
        super().integer_validation("height", height)
        self.__width = width
        self.__width = height

    def __str__(self):
        """ return str rep of Rectangle object """
        return "[{}] {}/{}".format(__class__.name, self.__width, self.__height)

    def area(self):
        """ returns area of Rectangle object """
        return (self__width * self__height)
