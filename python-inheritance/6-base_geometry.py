#!/usr/bin/python3
""" countains some classes for basic geometry:
    BaseGeometry: define the basic rules"""


class BaseGeometry:
    """defines some basic geometry rules to be used in subclasses"""
    def area(self):
        raise Exception("area() is not implemented")
