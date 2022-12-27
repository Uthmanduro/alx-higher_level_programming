#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    copy = []
    for i in matrix:
        for j in i:
            print("{}".format(j), end=" ")
        print()
