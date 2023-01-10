#!/usr/bin/python3
"""
    Defines a duntion that reads a text file and prints it to standard output
"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read(), end="")
