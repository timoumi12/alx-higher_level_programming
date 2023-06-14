#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    s = 0
    for i in new:
        s += i
    return (s)
