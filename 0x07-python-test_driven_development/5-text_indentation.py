#!/usr/bin/python3
"""
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ insert two lines after . : or ? """
    new_txt = ""
    flag = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_txt = text.replace(". ", ".")
    new_txt = new_txt.replace(": ", ":")
    new_txt = new_txt.replace("? ", "?")
    for char in new_txt:
        if char in [".", "?", ":"]:
            print(char)
            print()
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False
