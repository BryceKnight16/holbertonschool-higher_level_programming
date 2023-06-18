#!/usr/bin/python3
'''
Rectangle class example
'''


class Rectangle:
    '''
    Rectangle class with width and height
    '''

    number_of_rects = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''
        Instantiation of rectangle

        Arguments:
        width
        height
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_rects += 1

    @property
    def width(self):
        '''Get width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width of rectangle'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Get height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set height of rectangle'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Returns perimeter of rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        '''Returns a string with # in the shape of rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rect_str += str(self.print_symbol)
            if i != self.height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        '''Returns a string describing the rectangle'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Deletes and returns message'''
        print("Bye rectangle...")
        Rectangle.number_of_rects -= 1
