#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a class square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size mut be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or not isinstance(value[0], int) \
                or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for shape in range(self.__size):
            print(" " * self.__position[0] + "#" * self.size)
