import sys
import math

dictionary = set()

non = set()

#for x in (input().split() for i in range(int(input()))):
#    dictionary += [x]

for i in range(int(input())):
    line = input().lower().strip().split()
    for x in line:
        dictionary.add(x)

for i in range(int(input())):
    line = input().lower().strip().split()
    for word in line:
        if word not in dictionary:
            non.add(word)

for x in non:
    print(x)
