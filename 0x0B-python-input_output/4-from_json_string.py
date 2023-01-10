#!/usr/bin/python3
"""
    Defines a function the returns an object (python data strucutre)
    represented by a string
"""


import json


def from_json_string(my_str):
    """defines the fromjson string function"""
    return json.loads(my_str)
