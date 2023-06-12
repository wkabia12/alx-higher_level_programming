#!/usr/bin/python3
"""
    Module for Square class that imports from Rectangle
"""


Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """
        Square class

        Methods:
            __init__ - initializes object
    """

    def __init__(self, size):
        """ initializes Square object """
        super().integer_validator("size", size)
        self.__size = size
