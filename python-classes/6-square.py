#!/usr/bin/python3
"""
    creating the square class
"""


class Square:
    """
    Defines a géometrical square.

    Args:
        __size (int): length of side
        __position (int,int): position of square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Defines _size

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[1] < 0 or position[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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

    size = property(get_size, set_size)

    def set_position(self, value):
        """
        Set new position of the square

        args:
            value ((int,int)): value of new position must be positive and is
                a tuple of x/y axis

        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[1] < 0 or value[0] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def get_position(self):
        """
        Return position of the square

        """
        return self.__position

    position = property(get_position, set_position)

    def my_print(self):
        if self.__size == 0:
            print()
        for space in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                for space in range(self.__position[0]):
                    print(end=' ')
                print("#", end='')
            print()
