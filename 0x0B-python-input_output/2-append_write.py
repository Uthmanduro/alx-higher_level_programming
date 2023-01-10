#!/usr/bin/python3
"""
    Defines a function that appends to a string at the end of the file
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends to a file"""
    with open(filename, mode='a', encoding='utf-8') as myfile:
        no_append = myfile.write(text)
        return (no_append)
