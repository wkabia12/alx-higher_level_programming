#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if (len(argv) < 2):
        print("0")
    else:
        arg_sum = 0
        for i in range(1, len(argv)):
            arg_sum += int(argv[i])
        print("{}".format(arg_sum))
