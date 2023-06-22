#!/usr/bin/python3
'''
Module that returns JSON rep string
'''


import json

def from_json_string(my_str):
    '''
    return the JSON representation of an object(python data structure)
    '''
    obj = json.loads(my_str)
    return obj
