#!/usr/bin/python3

"""Creating a module called 5-sqaure

"""


class Square:
    """ Initializes a Square instance.

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        position ()
        if position (value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range (self.position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
