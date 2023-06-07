#!/usr/bin/python3
"""
    Function that multiplies 2 matrices:

    Prototype: def matrix_mul(m_a, m_b):

"""


def matrix_mul(m_a, m_b):
    """ Validate m_a and m_b as list of lists """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    """ Validate non-empty matrices """
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    """ Validate elements as integers or floats """
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    """ Validate rectangular shape """
    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])
    if any(len(row) != num_cols_a for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if any(len(row) != num_cols_b for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    """ Validate matrices can be multiplied """
    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ Perform matrix multiplication """
    result = []
    for row_a in m_a:
        new_row = []
        for col in range(num_cols_b):
            element = sum(row_a[i] * m_b[i][col] for i in range(num_cols_a))
            new_row.append(element)
        result.append(new_row)

    return result
