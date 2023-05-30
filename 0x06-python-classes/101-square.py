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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

    def __str__(self):
        return self.my_print2()

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = (x, y)

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            i = self.__size
            while (i > 0):
                if self.__position[1] > 0:
                    print("" + "#" * self.__size)
                else:
                    print(" " * self.__position[0] + "#" * self.__size)
                i -= 1

    def my_print2(self):
        out = ""
        if self.__size == 0:
            return ""
        else:
            i = self.__size
            while (i > 0):
                if self.__position[1] > 0:
                    out += "" + "#" * self.__size + "\n"
                else:
                    out += " " * self.__position[0] + "#" * self.__size + "\n"
                i -= 1
            return out
