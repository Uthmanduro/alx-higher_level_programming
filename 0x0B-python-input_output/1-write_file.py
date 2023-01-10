#!/usr/bin/python3
"""
    writes a string to a text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a file"""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        number_written = myfile.write(text)
        return(number_written)
