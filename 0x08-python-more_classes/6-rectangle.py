#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width is 0 or self.height is 0:
            return 0
        return((self.width * 2) + (self.height * 2))

    def __str__(self):
        temp = ""
        if self.height is 0 or self.width is 0:
            return temp
        for i in range(self.height):
            for j in range(self.width):
                temp += '#'
            temp += '\n'
        temp = temp[:-1]
        return temp

    def __repr__(self):
        width = str(self.__width)
        height = str(self.__height)
        return 'Rectangle(' + width + ', ' + height + ')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
