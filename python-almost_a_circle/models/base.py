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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts dict to json string"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ converts list of object to json string saved in file with the name
            of the class of conveted objects (class must be subclass of base"""
        json_string = ""
        for instance in list_objs:
            json_string += instance.to_json_string(instance.to_dictionary())
            if instance is not list_objs[len(list_objs) - 1]:
                json_string += ", "
        filename = f"{list_objs[0].__class__.__name__}.json"
        with open(filename, "w") as filename:
            filename.write(f"[{json_string}]")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation: json_string"""
        return json.loads(json_string)
