import sys
import math

s = input()

ss = s.split(' ')

l = []

mod = len(ss)
if (len(ss) > 1):
    for i in range(len(ss)):
        l += [(int(ss[(mod + (i - 1)) % mod]) + int(ss[((mod + (i + 1)) % mod)]))]
else:
    l = ss

for i in range(len(l)):
    sys.stdout.write("{} ".format(l[i]))