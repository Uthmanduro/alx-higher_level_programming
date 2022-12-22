#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize instance attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the value of size object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the value of position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for shape in range(self.__size):
            if self.__position[1] > 0:
                print(" " * self.__position[0] + "#" * self.__size)
            else:
                print(" " * self.__position[0] + "#" * self.__size +
                      " " * self.position[1])
