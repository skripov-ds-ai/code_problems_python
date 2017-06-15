import sys
import math

s = input()
s = s.lower()
count = 0

a = {
    'g', 'c'
}

for i in range(len(s)):
    if s[i] in a:
        count += 1

print(count * 100 / len(s))