import sys
import math

arr = [int(i) for i in input().split()]

#arr.sort()

res = set()

for i in arr:
    if arr.count(i) != 1:
        res.add(str(i) + "")

print(' '.join(res))