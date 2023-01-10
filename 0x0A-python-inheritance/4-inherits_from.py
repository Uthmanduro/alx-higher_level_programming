#!/usr/bin/python3
"""Checks whether an object inherits from a base class"""


def inherits_from(obj, a_class):
    """defines the inherit from function"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
