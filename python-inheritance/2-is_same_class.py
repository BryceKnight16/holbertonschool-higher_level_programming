#!/usr/bin/python3
'''
Creating a function that checks if the object exactly an instance of the
specified class
'''


def is_same_class(obj, a_class):
    '''
    Function that returns true or false if the its the same instance
    of speficied class
    '''
    return type(obj) is a_class
