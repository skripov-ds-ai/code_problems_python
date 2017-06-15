import sys
import math

s = 0
counter = 0

while True:
    t = int(input())
    if t == 0:
        break
    s += t
    counter += 1

print(s)