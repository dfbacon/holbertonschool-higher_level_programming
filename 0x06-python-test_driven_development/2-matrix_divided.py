#!/usr/bin/python3
'''
This is the "matrix_divided" module.

The matrix_divided module supplies one function, matrix_divided(matrix, div).

'''


def matrix_divided(matrix, div):
    '''Return matrix with each value divided by @div

    matrix: matrix being evaluated
    div: divisor
    '''

    if matrix is []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if i is []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if isinstance(j, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new = []
    temp = []
    for i in matrix:
        for j in i:
            temp.append(round(j / div, 2))
        new.append(temp)
    return(new)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
