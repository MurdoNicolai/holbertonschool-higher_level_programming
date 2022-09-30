#!/usr/bin/python3
"""basic write function"""


def write_file(filename="", text=""):
    """reads and prints inputed file
    filename (string): file to write to
    text (string): what to write in file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
