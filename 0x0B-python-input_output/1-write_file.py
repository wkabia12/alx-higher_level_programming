#!/usr/bin/python3
'''
    module with function that writes to a text file
'''


def write_file(filename="", text=""):
    """
        write string to txt file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text)):
