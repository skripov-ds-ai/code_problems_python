import sys
import math

lst = [int(i) for i in input().split()]
x = int(input())

s = ""

if lst.count(x) == 0:
    s = "Отсутствует"
else:
    for i in range(len(lst)):
        if lst[i] == x:
            s += str(i) + " "

print(s)