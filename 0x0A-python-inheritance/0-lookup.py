#!/usr/bin/python3
"""Defines a functioon thats returns the list of availablel attributes and methods"""


def lookup(obj):
    """
        returns the list of available attributes and methods of an object
    """
    return dir(obj)
