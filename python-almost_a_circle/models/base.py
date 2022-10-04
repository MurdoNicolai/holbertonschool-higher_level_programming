#!/usr/bin/python3
""" contains the Base class """


import json


class Base:
    """ Serves as Base for the other classes of the project:
        id (int): is diffrent for each object."""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
