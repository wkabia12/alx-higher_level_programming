#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i, s = 0, 0
        while x > 0:
            try:
                print("{:d}".format(my_list[i]), end='')
            except (TypeError, ValueError):
                s += 1
            i += 1
            x -= 1
        print("")
        return (i - s)
    except IndexError:
        print("")
        return (i - s)
