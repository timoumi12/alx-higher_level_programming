#!/usr/bin/python3

"""
    2-matrix_divided function

    creates a function that adds two integers
"""


def matrix_divided(matrix, div):
    """dividing all elements of matrix while checking edge cases"""

    e = 'matrix must be a matrix (list of lists) of integers/floats'
    if not isinstance(matrix, list):
        raise TypeError(e)
    for row in matrix:
        if not isinstance(matrix, list):
            raise TypeError(e)

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(e)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new = []
    for row in matrix:
        rows = []
        for elem in row:
            rows.append(round((elem/div), 2))
        new.append(rows)
    return new
