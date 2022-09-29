#!/usr/bin/python3
a = 1024
b = 1024
del a
print (f"{id(b)}, {id(b)}")
del b
c = 1024
print (f"{id(c)}, {id(c)}")
