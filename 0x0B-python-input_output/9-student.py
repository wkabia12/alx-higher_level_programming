#!/usr/bin/python3
'''
    module that defines the class Student
'''


class Student:
    """
       Defines Studnet Class

       Methods:
           __init__ : intilizes Student Obj
           to_json : retrives dict rep of Student Obj
    """
    def __init__(self, first_name, last_name, age):
        """ init Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrives dict represtation """
        return self.__dict__
