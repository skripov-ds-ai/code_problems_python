import sys
import math
import re

name = "dataset_3380_5.txt"

with open(name, 'r') as read:
    a = read.readlines()

reg = '\t|\n'

b = re.split(reg, ' '.join(a))
b = (' '.join(b)).split()

print(b)
print()

d = {}

for i in range(0, len(b), 3):
    if b[i] not in d:
        d[b[i]] = [0] * 2
    d[b[i]][0] += int(b[i + 2])
    d[b[i]][1] += 1

for i in range(1, 12):
    if str(i) in d:
        print("{} {}".format(i, d[str(i)][0] / d[str(i)][1]))
    else:
        print("{} -".format(i))
