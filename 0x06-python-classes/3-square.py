#!/usr/bin/python3
"""class is called Suare."""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """constructor

        Args:
    size: size is the lenght of sideof Square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size

        def area(self):
            return self.__size ** 2
