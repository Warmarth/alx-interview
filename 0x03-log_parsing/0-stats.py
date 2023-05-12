#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

for line_number, line in enumerate(sys.stdin, 1):
    # Split the line into its components
    parts = line.split()
    if len(parts) != 10:
        # If the line format is invalid, skip it
        continue

    ip_address, _, _, date, _, method, path, _, code, size = parts

    try:
        code = str(code)
        size = int(size)
    except ValueError:
        # If the status code or file size is not an integer, skip the line
        continue

    # Update metrics
    if code in cache.keys():
        cache[code] += 1
    total_size += size

    # Print metrics every 10 lines
    counter += 1
    if counter == 10:
        counter = 0
        print('File size: {}'.format(total_size))
        for key, value in sorted(cache.items()):
            if value != 0:
                print('{}: {}'.format(key, value))
    else:
        print('File size: {}'.format(total_size))
        for key, value in sorted(cache.items()):
            if value != 0:
             print('{}: {}'.format(key, value))