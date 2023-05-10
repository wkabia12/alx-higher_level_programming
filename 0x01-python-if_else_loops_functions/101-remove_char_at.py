#!/usr/bin/python3
def remove_char_at(str, n):
    rm_indx = str[:n] + str[n+1:]

    return ("{}".format(rm_indx))
