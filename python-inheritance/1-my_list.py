#!/usr/bin/python3

'''
    Creating a class called MyList that inherits from the class list
'''


class MyList(list):
    '''
    A class that inheritance from built-in class list
    '''
    def print_sorted(self):
       '''
        Function that print the sorted list.
        '''
        print(sorted(self))
