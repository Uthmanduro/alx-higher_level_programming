#!/usr/bin/python3
"""
    Defines a function that add two integer together
"""


def add_integer(a, b=98):
    """
        Return an  integer on addition of a aand b

        Args:
        a: first inteer
        b: second argument

        >>> add_integer(20, 20)
        40
        >>> add_integer(2.0, 2.0)
        4
        >>> add_integer("s", 4)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return int(a + b)
