#!/usr/bin/python3
"""
pascal triangle defination file
"""
from math import factorial


def pascal_triangle(n):
    """ prints pascal's triangle with n rows"""
    if n <= 0:
        return []

    """ initialize rezult list"""
    result = []

    for i in range(n):
        """initialize row results"""
        row = []

        for j in range(i+1):
            """nCr = n!/((n-r)!*r!)"""
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        result.append(row)

    return result
