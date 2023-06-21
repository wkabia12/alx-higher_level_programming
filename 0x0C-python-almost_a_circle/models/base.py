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

    @staticmethod
    def from_json_string(json_string):
        """ return python list of json string representation """
        if type(json_string) != str and json_string is not None:
            raise TypeError
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string of list_objs to a file """
        if list_objs:
            lis = [obj.to_dictionary() for obj in list_objs]
            json_obj = cls.to_json_string(lis)
        else:
            json_obj = "[]"
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(json_obj)
