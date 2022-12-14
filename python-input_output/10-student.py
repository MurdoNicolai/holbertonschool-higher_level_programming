#!/usr/bin/python3
""" has class students"""


class Student():
    """student:
    first_name (string)
    last_name (string)
    age (int)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            newdict = {}
            for key in attrs:
                if self.__dict__.get(key):
                    newdict[key] = self.__dict__.get(key)
            return newdict
        else:
            return self.__dict__
