#!/usr/bin/python3
'''
    module with function that appends to a text file
'''


def append_write(filename="", text=""):
    """
        appends string to txt file
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return (file.write(text)):
