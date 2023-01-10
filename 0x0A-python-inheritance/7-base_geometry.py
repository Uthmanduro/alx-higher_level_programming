#!/usr/bin/python3
"""define an empty class"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the name and value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
