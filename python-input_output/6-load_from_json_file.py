#!/usr/bin/python3
"""function that reads from textfile the JSON representation of an object"""
import json


def load_from_json_file(filename):
    """returns that reads frome textfile the JSON representation of:
        my_obj (string) and creates it
        filename (sting): file to read to
    """
    with open(filename, "r") as filename:
        return json.load(filename)
