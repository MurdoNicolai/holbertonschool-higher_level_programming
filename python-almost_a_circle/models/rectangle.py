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
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    def get_width(self):
        """width getter"""
        return self.__width

    def set_width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def get_height(self):
        """height getter"""
        return self.__height

    def set_height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def get_x(self):
        """x getter"""
        return self.__x

    def set_x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_y(self):
        """Y getter"""
        return self.__y

    def set_y(self, y):
        """Y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    width = property(fget=get_width, fset=set_width)
    height = property(fget=get_height, fset=set_height)
    x = property(fget=get_x, fset=set_x)
    y = property(fget=get_y, fset=set_y)

    def area(self):
        return self.width * self.height


