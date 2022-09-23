"""contains a simple addition function to practice making test files
        """

#!/usr/bin/python3
def add_integer(a, b=98):
    """adds together to numbers (float or int):
        a: first number
        b: second number
        >>> add_integer(1, 2)
        3
        """
    if (not isinstance(a,int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b,int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    else:
        print(f"{int(a) + int(b)}")
