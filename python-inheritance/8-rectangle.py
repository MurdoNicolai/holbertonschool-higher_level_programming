#!/usr/bin/python3
""" countains some classes for basic geometry:
    BaseGeometry: define the basic rules
    Rectangle(BaseGeometry): defines a rectangle"""


class BaseGeometry:
    """defines some basic geometry rules to be used in subclasses"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """defines some basic geometry rules for rectangles:
    height (int): hight of rectangle
    width (int): width of rectangle
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(BaseGeometry, "__width", width)
        BaseGeometry.integer_validator(BaseGeometry, "__height", height)
        self.__width = width
        self.__height = height
