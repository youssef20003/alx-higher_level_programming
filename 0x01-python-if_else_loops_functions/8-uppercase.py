#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c >= 97 and c <= 122:
            c -= 32
            c = chr(c)
            print("{}".format(c), end="")
