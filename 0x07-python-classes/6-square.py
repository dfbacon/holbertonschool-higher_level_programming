#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
            type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size > 0:
            print("\n" * self.__position[1], end="")
            print("\n".join((" " * self.__position[0]) + "#" * self.__size
                            for i in range(self.__size)))
        else:
            print()
