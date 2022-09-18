#!/usr/bin/python3
def best_score(a_dictionary):
    max = (None, 0)
    if not a_dictionary:
        return None
    for value in a_dictionary.items():
        if value[1] > max[1]:
            max = value
    return max[0]
