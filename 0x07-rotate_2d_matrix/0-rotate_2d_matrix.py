#!/usr/bin/python3
""" Function rotating 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix by 90 degrees clockwise in-place."""
    n = len(matrix)

    # Reverse the matrix, row-wise
    for i in range(n // 2):
        matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
