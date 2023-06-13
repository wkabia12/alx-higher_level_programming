#!/usr/bin/python3
'''
    module that defines the class Student
'''


class Student:
    """
       Defines Student Class
       Methods:
           __init__ : intilizes Student Obj
           to_json : retrives dict rep of Student Obj
    """
    def __init__(self, first_name, last_name, age):
        """ init Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrives dict represtation """
        _dict = {}
        if type(attrs) != list:
            return self.__dict__
        else:
            for attr in attrs:
                if type(attr) != str:
                    return self.__dict__
            for attr in self.__dict__:
                if attr in attrs:
                    _dict[attr] = self.__dict__[attr]
        return _dict
