#!/usr/bin/python3
"""basic read function"""


def read_file(filename=""):
    """reads and prints inputed file
        filename (string): file to read"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
