#!/usr/bin/python3
'''
Module for a function that return list
'''


def lookup(obj):
    '''
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj: The object to inspect

    Returns:
    A list of attribute and method names.

    '''
    return dir(obj)
