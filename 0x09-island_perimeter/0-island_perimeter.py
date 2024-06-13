#!/usr/bin/python3
"""Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """It calculate perimeter of the island in given grid.

    Args:
        grid (list of list of int): 2D grid of 0s and 1s.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        x = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == x - 1 or (x > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
