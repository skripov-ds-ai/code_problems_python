import sys
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
    sys.stdout.write("\t{}".format(i))
print()

for i in range(a, b + 1):
    sys.stdout.write("{}\t".format(i))
    for j in range(c, d + 1):
        sys.stdout.write("{}\t".format(i * j))
    print()