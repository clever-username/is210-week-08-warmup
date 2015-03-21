#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program modifies the Fibonacci function."""


def fibonacci(maxint):
    """This while loop takes an integer and generates a list.

    Args:
        maxint(int): Maximum value for the interations of loop.

    Returns:
        list(list):  List of generated values.

    Examples:
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8]

        >>> fibonacci(7)
        [0, 1, 1, 2, 3, 5]
        >>>
    """

    int_1, int_2 = 0, 1
    list = [int_1]
    while int_2 < maxint:
        list.append(int_2)
        int_1, int_2 = int_2, int_1 + int_2
    return list
