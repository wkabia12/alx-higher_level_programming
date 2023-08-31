#!/usr/bin/python3
""" find peak in list"""
    

def find_peak(list_of_integers):
    """ Find peak in integer list """
    if not list_of_integers:
        return None
    else:
        return max(list_of_integers)
