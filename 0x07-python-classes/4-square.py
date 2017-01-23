#!/usr/bin/python3
'''
This is the "4-square" module.

The 4-square module supplies one class and **number** of methods.
Class: Square
Methods:

'''


class Square:
    '''This is the "Square" class.

    The Square class computes the are of a square of a given size.

    The size must be of integer type, and be greater-than or equal to 0.
    '''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.size ** 2
