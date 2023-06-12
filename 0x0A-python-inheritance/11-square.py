#!/usr/bin/python
"""
   Module for Square class that imports from Rect
"""


Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """
        Square class

        Methods:
            __init__ - initializes object
            __str__ - str rep object
            area - returns area of object
    """

    def __init__(self, size):
        """ initializes Square object """
        super().integer_validation("size", size)
        self.__size = size

    def __str__(self):
        """ return str rep of Square object """
        return "[{}] {}/{}".format(__class__.name, self.__size, self.__size)

    def area(self):
        """ returns area of Square object """
        return (self__size ** 2)
