import sys
import math

while True:
    n = int(input())
    if (n > 100):
        break
    if (n < 10):
        continue
    print(n)