#!/usr/bin/python3
"""
    creating the square class
"""


class Square:
    """
    Defines a géometrical square.

    Args:
        __size (int): length of side

    """
    def __init__(self, size=0):
        """
        Defines _size

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

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
