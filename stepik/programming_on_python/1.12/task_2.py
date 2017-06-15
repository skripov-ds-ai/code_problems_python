import sys
import math

x = int(input())

ok = (x > -15) and (x <= 12) or (x > 14) and (x < 17) or (x >= 19)

print(ok)