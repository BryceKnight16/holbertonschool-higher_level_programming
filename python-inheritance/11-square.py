#!/usr/bin/python3
'''
Creating module for the subclass called Square
that inherits the parent class BaseGeometry
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''
    Initializes a Square class that inherits from rectangle.

    '''


    def __init__(self, size):
        '''
        Initializes a Square instance with the size as a
        parameter and then validates it with the
        integer_validator
        '''

        self.__size = size
        BaseGeometry().integer_validator("size", size)

    def area(self):
        '''
        Function that returns the area of the square
        '''

        return self.__size ** 2

    def __str__(self):
        '''
        function that prints a statement using __str__
        bout the square and the area
        '''
        return f"[Square] {self.__size}/{self.__size}"
