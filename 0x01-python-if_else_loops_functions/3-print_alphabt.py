#!/usr/bin/python3
i = 0
while i < 26:
    if chr((ord('a') + i)) not in 'eq':
        print("{}".format(chr(ord('a') + i)), end='')
    i += 1
