#!/usr/bin/python3
for char in range(97, 123):
    if char != ord('q') and char != ord('e'):
        print("{}".format(chr(char)), end='')
