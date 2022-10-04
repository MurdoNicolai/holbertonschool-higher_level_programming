#!/usr/bin/python3
"""containse the rectangle class"""


from models.base import Base

class Rectangle(Base):
    """Defines a rectangle:
        __width (int): width of rectangle
        __hight (int): hight of rectangle
        __x (int):
        __y (int):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """width getter"""
        return self.__width

    def set_width(self, width):
        """width setter"""
        self.__width = width

    def get_height(self):
        """height getter"""
        return self.__height

    def set_height(self, height):
        """height setter"""
        self.__height = height

    def get_x(self):
        """x getter"""
        return self.__x

    def set_x(self, x):
        """x setter"""
        self.__x = x

    def get_y(self):
        """Y getter"""
        return self.__y

    def set_y(self, y):
        """Y setter"""
        self.__y = y

    width = property(fget=get_width, fset=set_width)
    height = property(fget=get_height, fset=set_height)
    x = property(fget=get_x, fset=set_x)
    y = property(fget=get_y, fset=set_y)
