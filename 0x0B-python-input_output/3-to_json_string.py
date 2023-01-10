#!/usr/bin/python3
"""
    Defines function tha returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """returns the json representation of the object passed"""
    return json.dumps(my_obj)
