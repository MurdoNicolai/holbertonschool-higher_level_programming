#!/usr/bin/python3
""" countains some classes for basic geometry:
    Square(Rectangle): defines a square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines some basic geometry rules for rectangles:
    size (int): hight and width of square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = self._Rectangle__width


def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")
