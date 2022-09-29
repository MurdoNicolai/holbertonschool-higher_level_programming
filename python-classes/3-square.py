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
        return area of square

        """
        return self.__size ** 2
