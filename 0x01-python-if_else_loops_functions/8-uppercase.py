#!/usr/bin/python3
def uppercase(c):
	to_upper = ""
	for l in c:
		if l.isalpha() and ord(l) > 90:
			to_upper += chr(ord(l) - 32)
		else:
			to_upper += l

	print(f"{to_upper}")
