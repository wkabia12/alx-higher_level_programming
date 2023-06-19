#!/usr/bin/python3
"""
    Module that contains the class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Defines the Square Class

        Attributes:

        Methods:
            __init__ - init Square Class obj
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ init method for Square obj """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str rep for Square obj """
        return "[Square] ({}) {}/{} - {}/{}".format(self.__id,\
			self.__x, self.__y, self.__width, \
			self.__height)
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update id, width, height, x and y """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[1] if len(args) >= 2 else self.height
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return dict representation of a square """
        i = self.id
        w = self.width
        x = self.x
        y = self.y
        _dict = {'id': i, 'size': w, 'x': x, 'y': y}
        return _dict
