#!/usr/bin/python3
"""has function that returns description for JSON serialization of an object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object:
        obj (object): object to describe
    """
    return obj.__dict__
