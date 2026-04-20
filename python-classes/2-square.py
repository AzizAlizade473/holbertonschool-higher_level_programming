#!/usr/bin/python3
"""This module defines a Square class with size validation.

This module provides a simple Square class that allows instantiation
with an optional size (default is 0). The size must be a non-negative integer.
"""


class Square:
    """Defines a square by its size with validation.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
