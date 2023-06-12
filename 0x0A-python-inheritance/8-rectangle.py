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
    """

    def __init__(self, width, height):
        """ initializes Rectangle object """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__width = height
