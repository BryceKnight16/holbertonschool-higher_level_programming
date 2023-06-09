#!/usr/bin/python3
'''
Module that is a class that is a sqaure that inherits from the subclass
rectangle
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Represents a square shape, which is a special type of rectangle
    with equal width and height. Inherits from the Rectangle class.
    '''

    def __init__(self, size, x=0, y=0, id=None):
       '''
        Initializes a Square object.

        Args:
            size (int): The size (width/height) of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier of the square.
        '''
       super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
        Returns a string representation of the Square object.
        '''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''
        Retrieve size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Set size
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Updates the attributes of the square based
        on the provided arguments or keyword arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        '''
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns a dictionary representation of the Square object.
        '''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
