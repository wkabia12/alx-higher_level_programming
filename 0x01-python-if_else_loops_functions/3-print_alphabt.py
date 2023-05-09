#!/usr/bin/python3
i = 0
while i < 26:
	if chr((ord('a') + i)) != 'e' and chr((ord('a') + i)) != 'q':
		print(f"{chr(ord('a') + i)}",end = '')
	i += 1
