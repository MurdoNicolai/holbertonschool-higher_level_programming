#!/usr/bin/python3
"""basic append function"""


def append_write(filename="", text=""):
    """reads and prints inputed file
    filename (string): file to write to
    text (string): what to write in file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
