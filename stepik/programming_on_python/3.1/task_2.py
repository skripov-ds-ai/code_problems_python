import sys
import math


def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] //= 2
        else:
            l.pop(i)

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [2, 2, 3]
modify_list(lst)
print(lst)               # [2]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)