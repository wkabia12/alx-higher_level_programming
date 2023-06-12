#!/usr/bin/python3
'''
    module for function that returns True if object is
    a subclass of a_class else false
'''


def inherits_from(obj, a_class):
    """
        return True if obj inherits a_class, else False
    """
    return issubclass(type(obj), a_class) and (type(obj) != a_class)
