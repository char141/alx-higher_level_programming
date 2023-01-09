#!/usr/bin/python3
"""
Contains the MyList class.
"""


class MyList(list):
    """Subclass of list"""

    def __init__(self):
        """Initiatizes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
