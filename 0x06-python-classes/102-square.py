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
        __init__: initializes object
        area: Returns area of Square

    Description:
        The `Square` class is used to define a square object.
        It has a private attribute __size and a method to calculate the area.

    Example:
    >>> my_square = Square()
    """

    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
