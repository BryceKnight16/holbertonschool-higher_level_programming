#!/usr/bin/python3
'''
A module a script that adds all arguments to a Python list,
and then save them to a file
'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    load_from_json_file('add_item.json')
    file_exists = True
except FileNotFoundError:
    file_exists = False

if file_exists:
    data = load_from_json_file('add_item.json')
else:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, 'add_item.json')
