#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    _len = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="");
            _len += 1
        except IndexError:
            break
    if _len > 0:
        print("")
    return (_len)
