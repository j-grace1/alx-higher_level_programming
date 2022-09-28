#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            a = matrix[i][j]
            matrix[i][j] = a**2
    return matrix
