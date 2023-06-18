#!usr/bin/python3
"""
    Module that contains the class Rectangle
"""


class Rectangle(Base):
    """
        Defines the Rectangle Class

        Attributes:
            __width - width of Rect obj
            __height - height of Rect obj
            __x -
            __y -

        Methods:
            __init__ - init Rect Class obj
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init method for Rectangle obj """
        super().__init__(id)
        self.__width = width
        self.__height = width
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in self.__height:
            print("#" * __width)
