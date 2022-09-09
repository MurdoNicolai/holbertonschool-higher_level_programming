#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    for args in dir(hidden_4):
        if args[1] != '_':
            print(f"{args}".format())
