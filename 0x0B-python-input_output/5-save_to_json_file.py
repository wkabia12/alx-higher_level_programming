#!/usr/bin/python3
'''
    module that writes an object to a text file
'''


import json


def save_to_json_file(my_obj, filename):
    """
       writes object to text file
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
