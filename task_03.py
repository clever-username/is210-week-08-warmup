#! usr/bin/env python
# -*- coding: utf-8 -*-
"""This program calculates max, min, avg length of words for given arg."""

import decimal


def lexicographics(to_analyze):
    """This function calculates max, min and avg number of words in str.

    Args:
        to_analyze(str): String used to calculate length.

    Returns:
        data(tuple): Tuple with max, min and avg values .

    Example:
        >>> lexicographics(data.SHAKESPEARE)
        (12, 5, Decimal('8.14'))

    """

    this_str = to_analyze.split('\n')
    data = []
    for item in this_str:
        dvalue = len(item.split())
        data.append(dvalue)
    return (max(data), min(data), sum(data)/decimal.Decimal(len(data)))
