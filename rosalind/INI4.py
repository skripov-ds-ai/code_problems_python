import for_input_and_output
import sys
import math


file = for_input_and_output.read_file("ini4")

s = [int(x) for x in file[0].split()]

a, b = s[0], s[1]

if a % 2 == 0:
    a += 1

summ = 0

for i in range(a, b + 1, 2):
    # print(i)
    summ += i

print(summ)
