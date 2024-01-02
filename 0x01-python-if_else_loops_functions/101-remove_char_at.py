#!/usr/bin/python3
def remove_char_at(str, n):
    copy_str = str
    return "".join([char for char in copy_str if copy_str.index(char) != n])
