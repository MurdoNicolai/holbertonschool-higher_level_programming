 #!/usr/bin/python3
"""containse the rectangle class"""


from models.base import Base

class rectangle(Base):
    """Defines a rectangle:
        __width (int): width of rectangle
        __hight (int): hight of rectangle
        __x (int):
        __y (int):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    property(fget=get_width, fset=set_width)
    property(fget=get_height, fset=set_height)
    property(fget=get_x, fset=set_x)
    property(fget=get_y, fset=set_y)
