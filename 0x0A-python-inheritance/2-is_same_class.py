#!/usr/bin/python3
'''
    module for function that returns True if object is
    exactly instance of a class else false
'''


def is_same_class(obj, a_class):
    """
        return True if obj is instance of a_class, else False
    """
    return (type(obj) is a_class)
