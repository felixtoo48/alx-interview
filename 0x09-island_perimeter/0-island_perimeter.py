#!/usr/bin/python3
""" Island perimeter """


def island_perimeter(grid):
    """ Function that returns the perimeter of an island
    described in grid
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

            # removing connecting edges horizontal or vertically
            # if adjacent land is present
            if i > 0 and grid[i - 1][j] == 1:
                perimeter -= 2
            if j > 0 and grid[i][j - 1] == 1:
                perimeter -= 2
        return perimeter
