import sys
import math

b = 0

string = []

input_str = input()

end = 'end'

while input_str != end:
    b += 1
    tmp = [int(x) for x in input_str.split()]
    string.append(tmp)
    input_str = input()

a = len(string[0])

for i in range(b):
    for j in range(a):
        cross_sum = string[i][j - 1] + string[i][j + 1 - a] + string[i - 1][j] + string[i + 1 - b][j]
        print(cross_sum, end=' ')
    print()
