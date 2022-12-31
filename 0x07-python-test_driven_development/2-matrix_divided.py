#!/usr/bin/python3
"""
    Function that divides all elements of a mattrix
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix

        Returns a new matrix

        Args:
            matrix: 2d list of the arguments
            div: a number
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of \
integer/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for items in matrix:
        if not isinstance(items, list):
            raise TypeError("matrix must be a matrix (list of lists) of \
integer/floats")
        if len(matrix[0]) != len(items):
            raise TypeError("Each row of the matrix must have the same size")
    arr = [x[:] for x in matrix]
    for array in arr:
        for number in range(len(array)):
            if not isinstance(array[number], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
integer/floats")
            array[number] = round(array[number]/div, 2)
    return arr
