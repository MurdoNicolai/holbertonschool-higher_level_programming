#!/usr/bin/python3
from cgitb import reset


def roman_to_int(roman_string):
    dict_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string)
    result = 0
    if not roman_string:
        return 0
    for idx in range(len(roman_list) - 1):
        if roman_list[idx] not in dict_nums.keys():
            return 0
        if dict_nums.get(roman_list[idx]) < dict_nums.get(roman_list[idx + 1]):
            result -= dict_nums.get(roman_list[idx])
        else:
            result += dict_nums.get(roman_list[idx])
    result += dict_nums.get(roman_list[len(roman_list) - 1])
    return (result)
