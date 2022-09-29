#!/usr/bin/python3
"""has the is_same_class function which test if obj is a certain class
    or inherits forme that class"""


def is_kind_of_class(obj, a_class):
    """test if object is inheritant of a certain class or is that class:
        obj: object to test
        a_class: the class it should inherit frome or be
        return: true or false"""
    return (isinstance(obj) is a_class)

