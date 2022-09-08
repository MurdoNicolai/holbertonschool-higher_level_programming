#!/usr/bin/python3
from hashlib import new


def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return (str)
    newstr = []
    for i in range (len(str) - 1):
        newstr.append(str[i + (i >= n)])
    return("".join(newstr))
