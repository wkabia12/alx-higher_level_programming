#!/usr/bin/python3
def roman_to_int(roman_string):
    rdict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rsum = 0
    rlen = len(roman_string)
    if type(roman_string) != str or roman_string is None:
        return None
    for i in range(rlen):
        if i != rlen - 1 and rdict[roman_string[i]] < rdict[roman_string[i+1]]:
            rsum -= rdict[roman_string[i]]
        else:
            rsum += rdict[roman_string[i]]
    return rsum
