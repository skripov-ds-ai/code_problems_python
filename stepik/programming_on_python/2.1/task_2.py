import sys
import math

a = int(input())
b = int(input())

def gcd(a, b):
    while (b):
        a %= b
        a, b = b, a
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

print(lcm(a, b))