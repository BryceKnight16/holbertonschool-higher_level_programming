#!/usr/bin/python3
'''
A module a script that adds all arguments to a Python list,
and then save them to a file
'''

import sys
import json
import os.path

def save_to_json_file(my_obj, filename):
     '''
     Function that writes an Object to a text file,
     using a JSON representation
     '''
     with open(filename, 'w', encoding="utf-8") as f:
         f.write(json.dumps(my_obj))

def load_from_json_file(filename):
    """Create object from JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

add_item = "add_item.json"

if os.path.isfile(add_item):
    obj = load_from_json_file(add_item)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, add_item)
