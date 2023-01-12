#!/usr/bin/python3
"""define an empty class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclasss of the basegeometry class"""
    def __init__(self, width, height):
        """initialize the constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
