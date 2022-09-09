#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    i = 0
    import sys
    print(f"{len(argv) - 1} arguments:".format())

    for args in sys.argv:
        if i != 0:
            print(f"{i}: {args}".format())
        i += 1
