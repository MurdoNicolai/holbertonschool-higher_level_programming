#!/usr/bin/python3
def common_elements(set_1, set_2):
    newset = set()
    for elem1 in set_1:
        for elem2 in set_2:
            if elem1 == elem2:
                newset.add(elem1)
    return newset
