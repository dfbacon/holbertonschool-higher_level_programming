#!/usr/bin/python3
'''
This is the "4-square" module.

The 4-square module supplies one class and four  methods.
Class: Square
Methods: __init__(self, size=0)
         size(self)
         size(self, value)
         area(self)

'''


class Square:
    '''This is the "Square" class.

    The Square class computes the are of a square of a given size.

    The size must be of integer type, and be greater-than or equal to 0.
    '''

    def __init__(self, size=0):
        '''The __init__ method initializes the size object
        '''
        self.size = size

    @property
    def size(self):
        '''The size method sets size object as private
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''The size method checks value for type int and value >= 0
        '''
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''The area function returns the area (size**2) of the square
        '''
        return self.size ** 2
