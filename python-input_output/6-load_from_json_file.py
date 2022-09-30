#!/usr/bin/python3
"""function that reads from textfile the JSON representation of an object"""
import json


def save_to_json_file(my_obj, filename):
    """returns that reads frome textfile the JSON representation of:
        my_obj (string) and creates it
        filename (sting): file to read to
    """
    with open(filename, "r") as filename:
        json.load(my_obj, filename)
