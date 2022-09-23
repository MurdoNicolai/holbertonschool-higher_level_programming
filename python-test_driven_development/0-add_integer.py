#!/usr/bin/python3
"""contains a simple addition function to practice making test files"""


def add_integer(a, b=98):
    """adds together to numbers (float or int):
        a: first number
        b: second number
        """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
