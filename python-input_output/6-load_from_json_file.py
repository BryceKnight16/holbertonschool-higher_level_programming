#!/usr/bin/python3
'''
A module that creates an Object from a “JSON file”
'''

import json

def load_from_json_file(filename):
     '''
     Function that creates an Object from a “JSON file”
     '''
     with open(filename, 'r', encoding="utf-8") as f:
        jfile = json.load(f)
        return jfile