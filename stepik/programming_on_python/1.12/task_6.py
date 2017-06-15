import sys
import math

n = int(input())

s = "программист"

div = (n // 10) % 10
mod = n % 10

a = {1}
b = {2, 3, 4}

if (mod in a) and not (div in a):
    s = s
elif (mod in b) and not (div in a):
    s += "а"
else:
    s += "ов"

s = str(n) + " " + s

print(s)