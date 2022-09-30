#!/usr/bin/python3
""" countains some classes for basic geometry:
    BaseGeometry: define the basic rules"""


class BaseGeometry:
    """defines some basic geometry rules to be used in subclasses"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not value is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

