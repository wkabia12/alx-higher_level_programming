#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    i = 0
    for r in matrix:
        res.append([])
        for c in r:
            res[i].append(c**2)
        i += 1
    return res
