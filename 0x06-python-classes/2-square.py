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
        __init__: initialiazies object

    Description:
        The `Square` class is used to define a square object.
        It does have __size attribute and __init__ method.

    Example:
    >>> my_square = Square()
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
