#!/usr/bin/python3
'''
A module that creates a class called Base.
'''


class Base:
    '''
    class that is the base start for other classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a Base instance

        Args:
        id (int): instance of id.
        '''
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod

    def to_json_string(list_dictionaries):
    '''
    static method that returns a json string rep of list_dictionaries
    '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string rep of list_objs to a file
        '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )
        with open(filename, "w") as filename:
            filename.write(json_string)
