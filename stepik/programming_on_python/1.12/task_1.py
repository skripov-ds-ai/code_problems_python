import sys
import math

a = int(input())
b = int(input())
c = int(input())

p = float(a + b + c) / 2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(s)