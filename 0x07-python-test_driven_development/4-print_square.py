#!/usr/bin/python3
"""
    This module defines the print square function
"""


def print_square(size):
    """
        This function prints a suqare with dimension of size
        Args:
            size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for item in range(size):
        print("#" * size)
