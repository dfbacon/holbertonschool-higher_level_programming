#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__set_size(size)

    def __get_size(self):
        return self.__size

    def __set_size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
