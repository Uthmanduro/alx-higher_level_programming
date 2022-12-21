#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square class"""
    def __init__(self, size):
        """Initializes an instance attribute"""
        self.__size = size

    @property
    def size(self):
        """Intialize a getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize a setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area"""
        return self.__size * self.__size
