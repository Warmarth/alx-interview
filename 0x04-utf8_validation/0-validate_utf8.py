#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0
    for num in data:
        binary_rep = format(num, '#010b')[-8:]
        if num_bytes == 0:
            mask = 1 << 7
            while( num & mask) != 0:
                num_bytes +=1
                mask >>= 1

            if num_bytes == 0:
                continue

            elif num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == '1' and binary_rep[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
