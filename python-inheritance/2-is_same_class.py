#!/usr/bin/python3
"""has the is_same_class function which test if obj is a certain class"""


def is_same_class(obj, a_class):
    """test if object if of certain class:
        obj: object to test
        a_class: the class it chould be
        return: true or false"""
    return (type(obj) is a_class)
