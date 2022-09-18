#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newset = set_1.union(set_2)
    for elem1 in set_1:
        for elem2 in set_2:
            if elem1 == elem2:
                newset.discard(elem1)
    return newset
