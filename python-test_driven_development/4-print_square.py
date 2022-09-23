#!/usr/bin/python3
""" now we try to print some graphics and test that """


def print_square(size):
    """ print a square of # of given size:
        size: size of square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
