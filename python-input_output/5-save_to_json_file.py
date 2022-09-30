#!/usr/bin/python3
"""has function that writes to textfile the JSON representation of an object"""
import json


def save_to_json_file(my_obj, filename):
    """returns that writes to textfile theJSON representation of:
        my_obj (string)
        filename (sting): file to write to
    """
    with open(filename, "w") as filename:
        json.dump(my_obj, filename)
