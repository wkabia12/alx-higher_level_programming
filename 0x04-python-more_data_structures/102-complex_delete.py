#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for item in a_dictionary.items():
        if item[1] == value:
            to_del.append(item[0])
    for item in to_del:
        a_dictionary.pop(item)
    return a_dictionary
