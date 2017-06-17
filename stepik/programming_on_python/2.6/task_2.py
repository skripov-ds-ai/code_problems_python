import sys
import math

n = int(input())

count = 0
c = 0
i = 1

while count < n:
    sys.stdout.write("{} ".format(i))
    count += 1
    c += 1
    if c == i:
        i += 1
        c = 0
