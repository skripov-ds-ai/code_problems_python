import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
problem_name = 'rna'
txt_name = directory + name_part + problem_name + extension

with open(txt_name, 'r') as read:
    s = read.readlines()[0]

s = s.replace("T", "U")

print(s)
