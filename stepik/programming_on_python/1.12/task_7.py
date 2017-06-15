import sys
import math

s = input()

def my_sum(s, a, b):
    res = 0
    for i in range(0, 3):
        res += int(s[a * b + i])
    return res

first = my_sum(s, 3, 0)
second = my_sum(s, 3, 1)

result = "Обычный"

if (first == second):
    result = "Счастливый"

print(result)

a = 0
i = 0
while i < 5:
    a += 1
    if i % 2 == 0:
        a += 2
    if i > 2:
        a += 3
    i = i + 1

print(a)