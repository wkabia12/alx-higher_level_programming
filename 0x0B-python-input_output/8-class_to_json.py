#!/usr/bin/python3
'''
    module that returns dict description with simple data structures
'''


def class_to_json(obj):
    """
       returns dict of a class to a json obj
    """
    return (obj.__dict__)
