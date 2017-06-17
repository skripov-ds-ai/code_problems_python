import sys
import math

s = 0
l = []

while True:
    t = int(input())
    l += [t]
    s += t
    if (s == 0):
        break

del s

s = 0

for i in l:
    s += i * i

print(s)