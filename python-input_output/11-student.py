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
        '''
        Retrieve a dictionary representation of a Student instance
        using the json method.

        Args:
            attrs (list): Optional. A list of attribute names to be retrieved.
            If not provided, all attributes are retrieved.

        Returns:
            dict: A dictionary containing the requested
            attributes of the Student instance.
        '''
        if attrs is None:
            return self.__dict__

        json_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

 
    def reload_from_json(self, json):
        '''
        Replace all attributes of the Student instance
        with values from a dictionary.

        Args:
            json (dict): A dictionary representing
            the attributes of a Student instance.
        '''
        for key, value in json.items():
            setattr(self, key, value)
