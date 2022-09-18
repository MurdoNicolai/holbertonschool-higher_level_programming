#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for idx in range(len(my_list)):
        check = 1
        for idxCheck in range(idx + 1, len(my_list)):
            if my_list[idx] == my_list[idxCheck]:
                check = 0
        if check:
            sum += my_list[idx]
    return sum
