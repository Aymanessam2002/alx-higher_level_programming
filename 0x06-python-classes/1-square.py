#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size):
        """
        size : no type/value verification
        ----------------------------
        Private instance attribute size
        """
        self.__size = size
