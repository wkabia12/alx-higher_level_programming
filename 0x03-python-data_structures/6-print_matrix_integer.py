#!/usr/bin/python3
def print_matrix_integer(my_list=[[]]):
    if len(my_list) < 1:
        print("{}".format())
    else:
        for lst in my_list:
            for i in range(len(lst)):
                if i == len(lst) - 1:
                    print("{} ".format(lst[i]))
                else:
                    print("{}".format(lst[i]), end=" ")
