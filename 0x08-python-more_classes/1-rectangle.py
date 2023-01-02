#!/usr/bin/python3
"""
    Defines a rectangle class
"""


class Rectangle:
    """Declare the classs rectangle"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """reutrns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must me an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must me an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
