#!/usr/bin/python3
"""
    Module for Myint class that imports from int
"""


class MyInt(int):
    """
        Square MyInt - inverts == and !=

        Methods:
            __eq__ - returns false when True
            __ne__ - returns True when False
    """

    def __eq__(self, other):
        """ returns false when Equal """
        if isinstance(self, type(other)):
            return False

    def __ne__(self, other):
        """ returns false when Equal """
        if isinstance(self, type(other)):
            return True
