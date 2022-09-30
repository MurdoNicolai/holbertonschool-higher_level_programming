#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    """ returns the list of lists of integers of tha pascal triangle:
        n: number of lines to return"""

    pascallist = list()
    for i in range(1, n + 1):
        line = list()
        for j in range (0, i):
            if j == 0 or j == i - 1:
                line.append(1)
            else:
                line.append(pascallist[i - 2][j] + pascallist[i - 2][j - 1])
        pascallist.append(line)
    return pascallist
