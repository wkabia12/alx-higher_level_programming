#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = list(tuple_a)
            tuple_a.append(0)
            tuple_a = tuple(tuple_a)
        else:
            tuple_a = list(tuple_a)
            tuple_a += [0, 0]
            tuple_a = tuple(tuple_a)
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = list(tuple_b)
            tuple_b.append(0)
            tuple_b = tuple(tuple_b)
        else:
            tuple_b = list(tuple_b)
            tuple_b += [0, 0]
            tuple_b = tuple(tuple_b)
    temp = []
    for i in range(2):
        temp.append(tuple_a[i] + tuple_b[i])
    temp = tuple(temp)
    return temp
