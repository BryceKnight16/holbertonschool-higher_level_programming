#!/usr/bin/python3
'''
A module a script that adds all arguments to a Python list,
and then save them to a file
'''

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv

try:
    new_list = load_from_json_file("add_item.json")
except:
    new_list = []

for arg in args[1:]:
    new_list.append(arg)

save_to_json_file(new_list, "add_item.json")
