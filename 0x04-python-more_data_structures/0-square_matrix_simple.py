#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = []
    for i in matrix:
        mtrx.append(list(map(lambda n: n*n, i)))
    return mtrx
