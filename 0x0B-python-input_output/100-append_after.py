#!/usr/bin/python3
'''
    function that inserts line of txt after each line of specific string
'''


def append_after(filename="", search_string="", new_string=""):
    """
        appends string after each line containing specific string
    """
    new_txt = ""
    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if line.find(search_string) != -1:
            new_txt += line + new_string
        else:
            new_txt += line
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(new_txt)
