#!/usr/bin/python3
"""Defines a function that checks whether the onject is the same class"""


def is_same_class(obj, a_class):
    """returns true if object is an instance of  the specifed class
        else false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
