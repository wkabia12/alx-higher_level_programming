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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            i = self.__size
            while (i > 0):
                print("#" * self.__size)
                i -= 1
