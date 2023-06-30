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
        x (int): The x-coordinate of the rectangle's position. Defaults to 0.
        y (int): The y-coordinate of the rectangle's position. Defaults to 0.
        id (int): The unique identifier of the rectangle. Defaults to None.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the width is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the height is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The new x-coordinate of the rectangle's position.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the x-coordinate is less than 0.
        '''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The new y-coordinate of the rectangle's position.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the y-coordinate is less than 0.
        '''

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Returns the area of the rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Print the Rectangle instance in stdout using the character #.
        '''
        for i in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return f"""[Rectangle] ({self.id}) {self.x}/{self.y} -
        {self.width}/{self.height}"""
