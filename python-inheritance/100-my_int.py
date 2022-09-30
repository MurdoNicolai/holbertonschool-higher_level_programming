#!/usr/bin/python3
""" creating a rebel my int class"""


class MyInt(int):
    """an int class that inverts == and !="""

    def __eq__(self, __x):
        return super().__ne__(__x)

    def __ne__(self, __x):
        return super().__eq__(__x)
