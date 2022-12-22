#!/usr/bin/python3
"""Define a class sqaure"""


class Square:
    """Creates a square class object"""

    def __init__(self, size=0):
        """Initialize the instance attributes"""
        self.__size = size

    @property
    def size(self):
        """Property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print(" ")
        for line in range(self.__size):
            print("#" * self.__size)
