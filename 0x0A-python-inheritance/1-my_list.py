#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Excutes sorted output from built in lists."""

    def print_sorted(self):
        """prints sorted lists """
        print(sorted(self))
