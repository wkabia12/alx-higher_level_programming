#!/usr/bin/python3
""" module for locked class """


class LockedClass:
    """ class only allows for one attribute first_name """
    __slots__ = ("first_name")
