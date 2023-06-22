#!/usr/bin/python3
'''
Module that returns JSON rep string
'''


import json

def to_json_string(my_obj):
    '''
    return the JSON representation of an object
    '''
    
    json_string = json.dumps(my_obj)
    return json_string
