#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if all(len(i) == 0 for i in matrix):
        print("$")
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" " if j != i[-1] else "$\n")
