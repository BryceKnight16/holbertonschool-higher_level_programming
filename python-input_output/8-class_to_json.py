#!/usr/bin/python3
'''
A Module returns a dict description
'''



def class_to_json(obj):
    '''
    function that returns the dictionary description
    '''
    return vars(obj)
