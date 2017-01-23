#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__set_size(size)

    def __get_size(self):
        return self.__size

    def __set_size(self, size):
        self.__size = size
