#!/usr/bin/python3
'''
    module that defines a pascal_triangle function
'''


def pascal_triangle(n):
    """
       Defines pascal triangle function using lists
    """
    tri = []
    if n <= 0:
        return tri

    tri.append([1])

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tri[i-1][j-1] + tri[i-1][j])
        row.append(1)
        tri.append(row)

    return tri
