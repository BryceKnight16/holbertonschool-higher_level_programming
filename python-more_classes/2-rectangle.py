#!/usr/bin/python3
"""
Class called Rectangle
"""


class Rectangle:
    """
    Rectangle class with width and height
    """

    def __init__(self, width=0, height=0):
        """
        init of rectangle

        arguments: width height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
