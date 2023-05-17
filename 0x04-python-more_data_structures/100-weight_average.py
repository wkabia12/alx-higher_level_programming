#!/usr/bin/python3
def weight_average(my_list=[]):
    i_sum = 0
    w_sum = 0
    for tup in my_list:
        i_sum += (tup[0] * tup[1])
        w_sum += tup[1]
    return (i_sum / w_sum)
