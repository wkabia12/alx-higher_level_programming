#!/usr/bin/python3
def print_matrix_integer(my_list=[[]]):
    if not my_list:
        print("{}".format(''))
    else:
        for lst in my_list:
            for i in range(len(lst)):
                if i == len(lst) - 1:
                    print("{:d}".format(lst[i]))
                else:
                    print("{:d}".format(lst[i]), end=" ")
