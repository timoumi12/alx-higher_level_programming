#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    key = list(a_dictionary.keys())[0]
    _max = a_dictionary[key]
    for i, j in a_dictionary.items():
        if j > _max:
            _max = j
            key = i
    return (key)
