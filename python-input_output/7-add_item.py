#!/usr/bin/python3
'''
A module a script that adds all arguments to a Python list,
and then save them to a file
'''

import sys


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

args = sys.argv
try:
    arg_list = load_from_json_file("add_item.json")
except:
    arg_list = []

for arg in args[1:]:
    arg_list.append(arg)

save_to_json_file(arg_list, "add_item.json")
