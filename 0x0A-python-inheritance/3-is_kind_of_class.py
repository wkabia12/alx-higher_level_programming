#!/usr/bin/python3
'''
    module for function that returns True if object is
    an instance of a class else false
'''


def is_kind_of_class(obj, a_class):
    """
        return True if obj is an instance of a_class, else False
    """
    return (isinstance(obj, a_class))
