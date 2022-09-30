#!/usr/bin/python3
"""has the is_same_class function which test if obj is a certain class
    or inherits forme that class directly or not"""


def inherits_from(obj, a_class):
    """test if object is inheritant of a certain classdirectly or not:
        obj: object to test
        a_class: the class it should inherit frome or be
        return: true or false"""
    return (isinstance(obj, a_class) or type(obj) is a_class)
