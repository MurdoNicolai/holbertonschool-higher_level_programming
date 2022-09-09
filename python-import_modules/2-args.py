#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    i = 0
    import sys
    print(f"{len(argv) - 1} argument".format(), end='')
    if (len(argv) - 1) == 0:
        print(".")
    elif (len(argv) - 1) == 1:
        print(":")
    else:
        print("s:")


    for args in sys.argv:
        if i != 0:
            print(f"{i}: {args}".format())
        i += 1
