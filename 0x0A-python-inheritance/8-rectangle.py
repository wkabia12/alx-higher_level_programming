#!/usr/bin/python
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
        super().integer_validation("width", width)
        super().integer_validation("height", height)
        self.__width = width
        self.__width = height
