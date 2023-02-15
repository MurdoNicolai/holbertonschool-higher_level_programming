#!/usr/bin/python3
a = [1, 2, 3, 4, 6, 9, 10, 70]
b = [1, 2, 5, 8, 9, 8, -30]

def find_medium(array1, array2):
    new_array = array1 + array2

    for i in range (0, len(new_array) - 2):
        for j in range (0 , len(new_array) - 1):
            if new_array[j] > new_array[j+1]:
                temp = new_array[j]
                new_array[j] = new_array[j+1]
                new_array[j+1] = temp

    if len(new_array) % 2 == 1:
        print (new_array[int((len(new_array) - 1) / 2)])
    else:
        print (new_array[int(len(new_array) / 2)])
        print (new_array[int((len(new_array) / 2) + 1)])

find_medium (a,b)


