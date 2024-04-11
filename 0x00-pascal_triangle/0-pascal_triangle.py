#!/usr/bin/python3
def pascal_triangle(n):
    '''Generates Pascal's triangle up to the nth row.'''
    triangle = []

    if not isinstance(n, int) or n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                left_val = prev_row[j - 1]
                right_val = prev_row[j] if j < len(prev_row) else 0
                row.append(left_val + right_val)
        triangle.append(row)

    return triangle
