#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _list = []
    for i in my_list:
        if i == search:
            _list += replace,
        else:
            _list += i,
    return (_list)
