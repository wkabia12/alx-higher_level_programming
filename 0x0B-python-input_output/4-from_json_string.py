#!/usr/bin/python3
'''
    module that returns an object rep of an JSON string
'''


import json


def from_json_string(my_str):
    """
        returns json rep of obj
    """
    return json.loads(my_str)
