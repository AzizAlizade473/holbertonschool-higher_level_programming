#!/usr/bin/python3

class Square:
    """Defines a square by its size"""

    def __init__(self, size):
        """Initialize a new Square
        
        Args:
            size (int): The size of the square (private attribute)
        """
        self.__size = size   # Private instance attribute
