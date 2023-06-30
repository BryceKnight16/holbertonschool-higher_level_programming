#!/usr/bin/python3
'''
A module that creates a class called Rectangle
that inherits from the parent class Base.
'''

from models.base import Base


class Rectangle(Base):
    '''
    A class representing a rectangle.

    Inherits from the Base class.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        '''
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    def set_width(self, width):
        '''
        Set the width of the rectangle.

        Args:
            width (int): The new width of the rectangle.
        '''
        self.__width = width

    def get_height(self):
        '''
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        '''
        return self.__height

    def set_height(self, height):
        '''
        Set the height of the rectangle.

        Args:
            height (int): The new height of the rectangle.
        '''
        self.__height = height

    def get_x(self):
        '''
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        '''
        return self.__x

    def set_x(self, x):
        '''
        Set the x-coordinate of the rectangle's position.

        Args:
            x (int): The new x-coordinate of the rectangle's position.
        '''
        self.__x = x

    def get_y(self):
        '''
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        '''
        return self.__y

    def set_y(self, y):
        '''
        Set the y-coordinate of the rectangle's position.

        Args:
            y (int): The new y-coordinate of the rectangle's position.
        '''
        self.__y = y