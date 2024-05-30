#!/usr/bin/python3
"""Its the 2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """It rotates 2D matrix 90 degrees clockwise in place.
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) == 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(len(row) == cols for row in matrix):
        return

    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
