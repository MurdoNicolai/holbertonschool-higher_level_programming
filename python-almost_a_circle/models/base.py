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
        if list_objs is None:
            list_objs = list()
        for instance in list_objs:
            json_string += instance.to_json_string(instance.to_dictionary())
            if instance is not list_objs[len(list_objs) - 1]:
                json_string += ", "
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as filename:
            filename.write(f"[{json_string}]")

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation: json_string"""
        if json_string is None or json_string == list():
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates a new instance of the class with
            all attributes from the dictionary."""
        try:
            new = cls(1)
        except TypeError:
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ loads the list of the JSON string representation: json_string"""
        try:
            with open(cls.__name__ + ".json", "r") as filename:
                newlist = cls.from_json_string(filename.read())
        except FileNotFoundError:
            newlist = list()
        instance_list = list()
        for dict in newlist:
            instance_list.append(cls.create(**dict))
        return instance_list
