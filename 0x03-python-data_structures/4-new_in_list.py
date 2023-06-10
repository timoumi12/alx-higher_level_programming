#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx < 0 or len(my_list) <= idx:
        return (copy)
    else:
        copy[idx] = element
        return (copy)
