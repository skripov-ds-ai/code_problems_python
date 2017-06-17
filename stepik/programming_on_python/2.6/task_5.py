import sys
import math


def condition(arr, array_size, ix, iy):
    return -1 < ix < array_size and -1 < iy < array_size and arr[ix][iy] is None


def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0

    arr = [[None] * n for j in range(n)]

    for i in range(n ** 2):
        arr[x][y] = i + 1
        ix, iy = x + dx, y + dy
        if condition(arr, n, ix, iy):
            x, y = ix, iy
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    return arr


def print_array(arr):
    n = range(len(arr))
    for j in n:
        for i in n:
            sys.stdout.write("{} ".format(arr[i][j]))
        print()


n = int(input())
print_array(spiral(n))
