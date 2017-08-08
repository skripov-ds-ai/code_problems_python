import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
problem_name = 'dna'
txt_name = directory + name_part + problem_name + extension

with open(txt_name, 'r') as read:
    s = read.readlines()[0]

result = ""

for x in 'ACGT':
    result += str(s.count(x)) + " "
result += "\n"

print(result)