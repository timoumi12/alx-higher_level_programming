#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    _max = my_list[0]
    for i in my_list:
        if i > _max:
            _max = i
    return (_max)
