import sys
import math

x, y = 0, 0

n, s, w, e = 'север', 'юг', 'запад', 'восток'


def app(string, x, y, step):
    if string == e:
        x += step
    elif string == w:
        x -= step
    elif string == n:
        y += step
    else:
        y -= step
    return x, y


for i in range(int(input())):
    l = input().strip().split()
    x, y = app(l[0], x, y, int(l[1]))

print("{} {}".format(x, y))
