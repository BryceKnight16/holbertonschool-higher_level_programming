#!/usr/bin/python3
'''
a function that returns True if the object is an instance
of a class that inherited from specifie class
'''


def inherits_from(obj, a_class):
    '''
    checking if obj is in a_class or if it is inherited
    '''

    
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
