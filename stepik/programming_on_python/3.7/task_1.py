import sys
import math

d = {}

delimiter = ';'

size = 5

for goal in (input().split(delimiter) for n in range(int(input()))):
    for i in (0, 2):
        if goal[i] not in d:
            d[goal[i]] = [0] * size
        d[goal[i]][0] += 1
        d[goal[i]][1] += goal[1 - i] > goal[3 - i]
        d[goal[i]][2] += goal[1] == goal[3]
        d[goal[i]][3] += goal[1 - i] < goal[3 - i]
        d[goal[i]][4] += (goal[1 - i] > goal[3 - i]) * 3 + (goal[1] == goal[3])

for team in d:
    print(team + ':', end='')
    for x in d[team]:
        print(x, end=' ')
    print()
