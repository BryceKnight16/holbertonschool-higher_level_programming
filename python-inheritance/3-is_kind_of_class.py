#!/usr/bin/python3
'''
Creating a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class of it is otherwise False.
'''

def is_kind_of_class(obj, a_class):
    '''
    function that returns true or false if its a subclass or instance
    '''
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
