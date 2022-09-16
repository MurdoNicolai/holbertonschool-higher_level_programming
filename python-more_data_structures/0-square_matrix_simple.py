#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    i = 0
    new_matrix = [[0 for x in matrix[0]] for y in matrix]
    for line in matrix:
        j = 0
        for n in line:
            new_matrix[i][j] = n ** 2
            j += 1
        i += 1
    return new_matrix
