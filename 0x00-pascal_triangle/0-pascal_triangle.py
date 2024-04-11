#!/usr/bin/python3
'''The Mod for working with Pascal triangle
'''


def pascal_triangle(n):
    '''It makes list of lists of integers repr
    Pascal's triangle of given integer
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle
