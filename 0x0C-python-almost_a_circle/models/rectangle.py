#!/usr/bin/python3
"""
    Module that contains the class Rectangle
"""


from models.base import Base


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

    def __str__(self):
        """ str rep for Rectangle obj """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.__id,\
			self.__x, self.__y, self.__width, \
			self.__height)

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
        for i in self.__y:
            print()
        for i in self.__height:
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args):
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return dict representation of a rectangle """
        i = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        _dict = {'id': i, 'width': w, 'height': h, 'x': x, 'y': y}
        return _dict
