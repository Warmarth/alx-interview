#!/usr/bin/python3
"""
0-island_perimeter.py file
"""


def island_perimeter(grid):
    """
    it get the number of rows in the grid
    returns the perimeter of the island described in grid
    """
    rows = len(grid)
    if rows == 0:
        return 0

    # get the number of columns in the grid
    columns = len(grid[0])
    perimeter = 0

    # iterate over each cell in the grid
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                # check top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # check bottom
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # check right
                if col == columns - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    # return the calculated perimeter
    return perimeter
