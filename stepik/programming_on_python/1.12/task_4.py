import sys
import math

string = input()

s = 0.0

a = int(input())

pi = 3.14

if string == 'круг':
    s = pi * (a ** 2)
else:
    b = int(input())
    if string == 'прямоугольник':
        s = a * b
    else:
        c = int(input())
        if string == 'треугольник':
            p = float(a + b + c) / 2
            s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(s)