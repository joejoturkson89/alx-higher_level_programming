#!/usr/bin/python3
"""Function that defines Pascal's Triangle."""


def pascal_triangle(n):
    """This represents Pascal's Triangle of size n."""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
