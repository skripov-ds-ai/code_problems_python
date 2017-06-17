import sys
import math

s1, s2, s3, s4 = input(), input(), input(), input()

res1, res2 = "", ""

for i in range(len(s3)):
    res1 += s2[s1.find(s3[i])]

for i in range(len(s4)):
    res2 += s1[s2.find(s4[i])]

print("{0}\n{1}".format(res1, res2))
