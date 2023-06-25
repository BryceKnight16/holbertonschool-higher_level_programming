#!/usr/bin/python3
'''
A module that prints a represtation of pascals triangle
'''

def pascal_triangle(n):
    '''
    Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    '''

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j] + prev_row[j - 1])
        row.append(1)
        triangle.append(row)

    return triangle
