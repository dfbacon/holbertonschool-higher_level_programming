#!/usr/bin/python3
'''
This is the "matrix_divided module.

The matrix_divided module supplies one function, matrix_divided(matrix, div).

'''
def matrix_divided(matrix, div):
    '''Return matrix with each value divided by @div
    '''
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix[j][i] /= div
            format(matrix[j][i], '.2f')
    return(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
