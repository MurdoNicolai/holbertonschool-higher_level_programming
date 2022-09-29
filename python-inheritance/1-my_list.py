#!/usr/bin/python3
"""Creating MyList that inherits frome list"""


class MyList(list):
    """inherits the list class but we add sorted print function:
        print_sorted (func): prints the lists but sorted without changes
    """
    def print_sorted(self):
        print(sorted(self))
