#!/usr/bin/python3
def uppercase(c):
    to_upper = ""
    for let in c:
        if let.isalpha() and ord(let) > 90:
            to_upper += chr(ord(let) - 32)
        else:
            to_upper += let

    print("{}".format(to_upper))
