#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program checks truthiness of an argument."""


def bool_to_str(bval):
    """This function takes one argument and evaluates truthiness.

    Args:
        bool_to_str(bool): Argument evaluated for truthiness or falsiness.

    Returns:
        my_bool(str): String returning Yes or No depending on truthiness.

    Examples:
        >>> bool_to_str(1)
        'Yes'

        >>> bool_to_str('')
        'No'

    """

    my_bool = ''
    if bval:
        my_bool = 'Yes'
    else:
        my_bool = 'No'
    return my_bool
