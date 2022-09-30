#!/usr/bin/python3
"""has function that returns description for JSON serialization of an object"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    for JSON serialization of an object:
        obj (object): object to describe
    """
    return json.encode(obj)
