#!/usr/bin/python3
"""just contains the revtangle class"""

class Square:
    """
    Defines a géometrical square.

    Args:
        __width (int): length of side
        __height (int): length of other side

    """
    def __init__(self, width=0, height=0):
        """
        Defines __width and __height

        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height


    def area(self):
        """
        Return area of the square

        """
        return self.__size ** 2

    def set_size(self, value):
        """
        Set new size of the square

        args:
            value (int): value of new size must be positive

        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def get_size(self):
        """
        Return size of the square

        """
        return self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()

    size = property(get_size, set_size)
