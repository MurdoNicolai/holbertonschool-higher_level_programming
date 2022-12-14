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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width*self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
