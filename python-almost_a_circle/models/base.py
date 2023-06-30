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
