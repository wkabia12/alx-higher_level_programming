#!/usr/bin/python3
"""
    Module for add attribute method
"""


def add_attribute(_object, _attribute, value):
    """ adds new attribute if possible """
    setattr(_object, _attribute, value)
