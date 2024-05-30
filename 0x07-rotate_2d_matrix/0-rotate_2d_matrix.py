#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_matrix_90_degrees_clockwise(matrix_2d):
    """Rotates a 2D matrix 90 degrees clockwise in place.
    """
    if not isinstance(matrix_2d, list):
        return
    if len(matrix_2d) == 0:
        return
    if not all(isinstance(row, list) for row in matrix_2d):
        return
    num_rows = len(matrix_2d)
    num_cols = len(matrix_2d[0])
    if not all(len(row) == num_cols for row in matrix_2d):
        return

    col_index, row_index = 0, num_rows - 1
    for cell_index in range(num_cols * num_rows):
        if cell_index % num_rows == 0:
            matrix_2d.append([])
        if row_index == -1:
            row_index = num_rows - 1
            col_index += 1
        matrix_2d[-1].append(matrix_2d[row_index][col_index])
        if col_index == num_cols - 1 and row_index >= -1:
            matrix_2d.pop(row_index)
        row_index -= 1
