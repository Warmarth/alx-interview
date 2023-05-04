#!/usr/bin/python3

def minOperations(n):
    """model performes only two functions copy all and paste
    H = single character
    n = number of times a character will be pasted{iterate}

    """
    md = 1
    copyall = 0
    paste = 0
    while md < n:
        remainder = n - md
        if (remainder % md == 0):
            copyall = md
            md += copyall
            paste += 2
        else:
            md += copyall
            paste += 1
    return paste
