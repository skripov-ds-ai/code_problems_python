import sys
import math

extension = '.txt'
directory = './input/'
txt_name = directory + "rosalind_dna" + extension

with open(txt_name, 'r') as read:
    s = read.readlines()[0]

result = ""

for x in 'ACGT':
    result += str(s.count(x)) + " "
result += "\n"

print(result)