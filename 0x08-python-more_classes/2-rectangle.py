#!/usr/bin/python3
'''
    Module defines Rectangle class
'''


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        height - height of recctangle
        width - width of recctangle

    Methods:
        __init__ - initialize Rectangle objects
        height - sets Rectangle height
        width - sets Rectangle width
        area - returns Rectangle area
        perimeter - returns Rectangle perimeter

    Description:
        The `Rectangle` class is used to define a Rectangle object.

    Example:
    >>> my_rect = Rectangle()
    """
    def __init__(self, width=0, height=0):
        """ initializes height and width """
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @height.setter
    def height(self, value):
        """ set height with new value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ set width with new value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns de area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
