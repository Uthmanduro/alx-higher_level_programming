#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for items in matrix:
        new = list(map(lambda x: x**2, [x for x in items]))
        new_matrix.append(new)
    return new_matrix
