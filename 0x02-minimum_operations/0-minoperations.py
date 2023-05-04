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
    copy = 0
    paste = 0
    for i in range(n):
        if now >= n:
            break
        remainder = n - now
        if remainder % now == 0:
            copy = now
            now += copy
            paste += 2
        else:
            now += copy
            paste += 1
    return paste

