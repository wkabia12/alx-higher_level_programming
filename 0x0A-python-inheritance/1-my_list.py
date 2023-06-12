#!/usr/bin/python3
'''
    Module defines Mylist which inherits from list
'''


class MyList(list):
    """
    Represents a MyList class which inherits from list.

    Attributes:
        None
    Methods:
        print_sorted - prints list in sorted order
    Description:
        The `Mylist` class is used to define a list object.

    Example:
    >>> my_rect = Rectangle()
    """
    def print_sorted(self):
        """ prints list is asc order """
        print(sorted(self))
