#!/usr/bin/python3
'''
A module that creates an Object to a text file,
using a JSON representation
'''


import json

def save_to_json_file(my_obj, filename):
     '''
     Function that writes an Object to a text file,
     using a JSON representation
     '''
     with open(filename, 'w', encoding="utf-8") as f:
          json.dumps(my_obj, f)
