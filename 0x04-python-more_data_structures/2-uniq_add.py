#!/usr/bin/python3
def uniq_add(my_list=[]):
    ans = 0
    uniq = []
    for i in my_list:
        if i not in uniq:
            uniq.append(i)
    for i in uniq:
        ans += i
    return ans
