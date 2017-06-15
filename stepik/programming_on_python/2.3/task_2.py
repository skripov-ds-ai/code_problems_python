import sys
import math

a = int(input())
b = int(input())

counter = 0
s = 0

for i in range(a, b + 1):
    if (i % 3 == 0):
        counter += 1
        s += i

print(s / counter)