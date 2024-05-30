#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if not all(map(lambda x: len(x) == num_cols, matrix)):
        return
    c, r = 0, num_rows - 1
    for i in range(num_cols * num_rows):
        if i % num_rows == 0:
            matrix.append([])
        if r == -1:
            r = num_rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == num_cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
