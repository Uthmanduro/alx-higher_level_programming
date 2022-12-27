#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = 0
    for integer in my_list:
        if integer > biggest:
            biggest = integer
    return biggest
