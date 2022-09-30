#!/usr/bin/python3
""" countains some classes for basic geometry:
    Rectangle(BaseGeometry): defines a rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines some basic geometry rules for rectangles:
    height (int): hight of rectangle
    width (int): width of rectangle
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(BaseGeometry, "width", width)
        BaseGeometry.integer_validator(BaseGeometry, "height", height)
        self.__width = width
        self.__height = height
