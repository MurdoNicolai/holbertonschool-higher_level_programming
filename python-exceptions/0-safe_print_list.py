#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for elem in my_list:
        if count < x:
            try:
                print(f"{elem}".format(), end = '')
            except:
                print("error")
            count += 1
    print()
    return count
