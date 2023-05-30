#!/usr/bin/python3
'''
    Module defines Square class
'''


class Square:
    """
    Represents a square.

    Attributes:
        __size: private attribute to store size variable

    Methods:
        __init__: initializes an object

    Description:
        The `Square` class is used to define a square object.
        It contains the __size attribute and __init__ meathod.

    Example:
    >>> my_square = Square(3)
    """
    def __init__(self, size):
        self.__size = size
