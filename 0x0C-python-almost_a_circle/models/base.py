#!/usr/bin/python3
"""
    Module that contains the class Base
"""


class Base():
    """
        Defines the Base Class

        Attributes:
            _nb_objects - couunts no of Base Obj instances

        Methods:
            __init__ - init Base Class obj
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
