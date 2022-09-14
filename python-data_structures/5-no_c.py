#!/usr/bin/python3
def no_c(my_string):
    idx = 0
    for char in my_string:
        if char == 'c' or char == 'C':
            my_string = my_string[0:idx] + my_string[idx + 1:]
        else:
            idx += 1
    return ''.join(my_string)
