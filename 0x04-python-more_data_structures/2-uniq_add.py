#!/usr/bin/python3
def uniq_add(my_list=[]):
    z = 0
    for item in set(my_list):
        z += item
    return z
