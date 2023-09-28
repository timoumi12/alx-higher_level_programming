#!/usr/bin/python3
'''finds a peak in a list of unsorted integers'''

def find_peak(list_of_integers):
    '''find peak function'''

    _list = list_of_integers
    _len = len(_list)
    if _list is None or _len == 0:
        return None

    if _len == 1 or _list[0] >= _list[1]:
        return _list[0]

    if _len == 2 and _list[-1] >= _list[-2]:
        return _list[-1]

    for i in range(1, _len - 1):
        if (_list[i] >= _list[i - 1] and _list[i] >= _list[i + 1]):
            return _list[i]

    if _list[-1] >= _list[-2]:
        return _list[-1]

    return None
