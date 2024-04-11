#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]  # First element in every row is 1
        if i > 0:
            # Calculate elements in the current row based on the previous row
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element in every row is 1
        triangle.append(row)

    return triangle
