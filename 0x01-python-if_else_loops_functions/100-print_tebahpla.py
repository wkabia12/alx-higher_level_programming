#!/usr/bin/python3
i = 0
while i < 26:
    if i % 2 == 0:
        print("{}".format(chr(ord('z') - i)), end='')
    else:
        print("{}".format(chr(ord('z') - i - 32)), end='')
    i += 1
