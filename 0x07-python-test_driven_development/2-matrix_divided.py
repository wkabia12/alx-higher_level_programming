#!/usr/bin/python3
"""
    Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ Divide a matrix by a number div """
    list_err = "matrix must be a matrix (list of lists) of integers/floats"
    len_err = "Each row of the matrix must have the same size"
    div_int_err = "div must be a number"
    div_zero_err = "division by zero"
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_err)
    if type(div) != int and type(div) != float:
        raise TypeError(div_int_err)
    if div == 0:
        raise ZeroDivisionError(div_zero_err)
    row_len = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError(list_err)
        if len(row) != row_len:
            raise TypeError(len_err)
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError(list_err)
            num = col / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
