#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for item in matrix[i]:
            print('{:d}'.format(item), sep=' ', end='\n')
        print('')
        i += 1
