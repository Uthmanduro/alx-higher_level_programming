#!/usr/bin/python3
"""
    Script that adds all arguments to a pyton list and then save them to a file
"""


import json
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
with open('add_item.json', mode='a', encoding='utf-8') as myfile:
    arr = load_from_json_file('add_item.json')
    save_to_json_file(arr + sys.argv[1:], 'add_item.json')
