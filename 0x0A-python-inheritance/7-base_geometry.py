#!/usr/bin/python3
"""
    Module for BaseGeometry class
"""


class BaseGeometry:
    """
        BaseGeometry class

        Methods:
            area - raises exeception
    """

    def area(self):
        """ raise exeception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value arg as int > 0 """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
