#!/usr/bin/python3
"""
    Defines the save to json function
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a json representation"""
    with open(filename, mode='w', encoding='utf-8') as myfile:
        json.dump(my_obj, myfile)
