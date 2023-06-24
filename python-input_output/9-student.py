#!/usr/bin/python3
'''
A module that has a class that defines a student
'''


class Student:
    '''
    Class that defines that student
    '''


    def __init__(self, first_name, last_name, age):
        '''
        Instantiation the class student
        with first_name, last_name and age
        '''


        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
            return vars(obj)
