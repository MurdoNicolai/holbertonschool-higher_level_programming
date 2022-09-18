#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for idx in range(list_length):
        try:
            new_list[idx] = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            new_list[idx] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[idx] = 0
        except IndexError:
            print(f"out of range: {idx}")
            new_list[idx] = 0
    return new_list
