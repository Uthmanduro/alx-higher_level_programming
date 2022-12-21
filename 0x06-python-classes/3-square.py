#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represents a square class"""
    def __init__(self, size=0):
        """Initializes an instance of a class
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
