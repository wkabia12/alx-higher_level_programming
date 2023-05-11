#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if (len(argv) < 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (argv[2] not in "+-*/"):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        arg_calc = 0
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]

        if (op == "+"):
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        if (op == "-"):
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        if (op == "*"):
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        if (op == "/"):
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
