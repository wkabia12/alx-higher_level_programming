#!/usr/bin/python3
def best_score(a_dictionary):
    name = None
    top = 0

    if a_dictionary is None:
        return None

    for item in a_dictionary.items():
        if item[1] > top:
            top = item[1]
            name = item[0]
    return name
