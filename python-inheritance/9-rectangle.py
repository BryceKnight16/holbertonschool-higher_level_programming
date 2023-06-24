#!/usr/bin/python3
'''
Creating module for the subclass called Rectangle
that inherits the parent class BaseGeometry
'''


class BaseGeometry:
    '''
    Creating class called BaseGeometry
    '''


    def area(self):
        '''
        Creating a function to raise an exception message
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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''
    Creating class called Rectangle that inherits BaseGeometry
    '''
    def __init__(self, width, height):
        '''
        Initializes a Rectangle object with the specified width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        '''


        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        '''
        Function thats gets the area of rectangle

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Returns:
        The area of the specified rectangle
        '''

        return self.__width * self.__height


    def __str__(self):
        '''
        function that prints a statement using __str__
        bout the rectangle and the area
        '''


        return f"[Rectangle] {self.__width}/{self.__height}"
