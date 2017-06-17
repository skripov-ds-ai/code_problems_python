import sys
import math

s = input()

ss = s.split(' ')

res = 0

for i in range(len(ss)):
    res += int(ss[i])

print(res)