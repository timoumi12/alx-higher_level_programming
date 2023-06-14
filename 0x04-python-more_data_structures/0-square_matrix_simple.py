#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for i in matrix:
        _list = []
        for j in i:
            _list += j ** 2,
        m += _list,
    return (m)
