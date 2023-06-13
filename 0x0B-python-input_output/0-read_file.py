#!/usr/bin/python3
'''
    module with function that reads a text file
'''


def read_file(filename=""):
    """
        reads a file and outputs to stdout
    """
    if filename:
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                print(line, end="")
