#!/usr/bin/python3
"""
pascal triangle defination file
"""
from math import factorial


def pascal_triangle(n):
    """ prints pascal's triangle with n rows"""
    for i in range(n):
        """loop to get leading spaces"""
        for j in range(n-i+1):
            print(end="")

        """loop to get elements for row i"""
        row = []
        for j in range(i+1):
            """nCr = n!/((n-r)!*r!)"""
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))

        print("[", end="")
        print(*row, sep=', ', end=']\n')
