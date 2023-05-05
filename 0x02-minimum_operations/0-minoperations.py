#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    now = 1
    start = now -1
    paste = now - 1
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            paste += 2
        else:
            now += start
            paste += 1
    return paste
