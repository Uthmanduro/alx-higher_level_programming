#!/usr/bin/python3
"""
    defines the load from json function
"""


import json


def load_from_json_file(filename):
    with open(filename, encoding='utf-8') as myfile:
        return json.load(myfile)
