#!/usr/bin/python3
'''
    module that creates an object from json file
'''


import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
args = sys.argv[1:]
fname = "add_item.json"

try:
    py_obj = load(fname)
except FileNotFoundError:
    save([], fname)

py_obj = load(fname)
if type(py_obj) is list:
    for arg in args:
        py_obj.append(arg)
save(py_obj, fname)
