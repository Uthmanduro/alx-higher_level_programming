#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """area is not implemented"""
        raise Exception("area() is not implemented")
