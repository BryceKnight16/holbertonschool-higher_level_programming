#!/usr/bin/python3
'''
Creating module for the class called BaseGeometry
'''


class BaseGeometry:
    '''
    Creating class called BaseGeometry
    '''
    def area(self):
        '''
        Creating a function to raise a expection message
        '''
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        '''
        Validate the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        '''
        if type(value) != int:
            raise TypeError (f"{name} must be an integer")
        if value <= 0:
            raise ValueError (f"{name} must be greater than 0")
