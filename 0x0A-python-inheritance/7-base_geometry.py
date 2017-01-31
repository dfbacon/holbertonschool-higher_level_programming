#!/usr/bin/python3
'''
This is the "7-base_geometry" module.

The module contains one class: "BaseGeometry"; and two methods: "area(self)",
and "integer_validator(self, name, value)".

'''


class BaseGeometry:
    '''This is the "BaseGeometry" class.
    '''
    def area(self):
        '''This is the "area" method.

        The area method takes only the self argument.

        area raises an exception.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''This is the "integer_validator" method.

        The integer_validator method takes two arguments beyond self:
        @name: a string
        @value: value being evaluated

        integer_validator raises exceptions if value is not of 'int' type and
        value is greater than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
