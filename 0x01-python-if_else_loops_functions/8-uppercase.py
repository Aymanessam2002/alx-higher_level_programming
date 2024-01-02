#!/usr/bin/python3
def uppercase(str):
    print("".join(['{:c}'.format(ord(char) - 32) if ord(char) in range(97, 123)
                   else char for char in str]))
