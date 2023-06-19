#!/usr/bin/python3
"""
    Module that contains the class Base
"""


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return json str of list of dicts """
        if type(list_dictionaries) != list and list_dictionaries is not None:
            raise TypeError
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for _dict in list_dictionaries:
            if type(_dict) != dict:
                raise TypeError
        return json.dumps(list_dictionaries)
