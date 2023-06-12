#!/usr/bin/python3
'''
    module with function to return all available attributes and meathods
'''


def lookup(obj):
    """
        return out all attributes and methods in object
    """
    return [mthd for mthd in dir(obj)]
