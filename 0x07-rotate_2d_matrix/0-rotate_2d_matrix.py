#!/usr/bin/python3
""" Function rotating 2D matrix 90 degree clockwise"""

N = 3


def rotate_2d_matrix(matrix):
    """ function to rotate 2D matrix by 90 degrees """
    global N

    for j in range(N):
        for i in range(N - 1, -1, -1):
            print(matrix[i][j], end=' ')
        print()
