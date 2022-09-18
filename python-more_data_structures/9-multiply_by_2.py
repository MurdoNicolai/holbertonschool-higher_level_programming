#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for value in a_dictionary.items():
        new_dictionary.update({value[0]: value[1] * 2})
    return new_dictionary
