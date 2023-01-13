#!/usr/bin/python3
"""the base class which is the base of all the other classe in this project"""


class Base:
    """Declaring the base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize the class constructor"""
        self.id = id
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
