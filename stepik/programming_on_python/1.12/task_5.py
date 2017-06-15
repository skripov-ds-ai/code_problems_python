import sys
import math

a = int(input())
b = int(input())
c = int(input())

max = max(a, b, c)
min = min(a, b, c)
mid = a + b + c - max - min

print("{}\n{}\n{}".format(max, min, mid))