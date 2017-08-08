import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
txt_name = directory + name_part + "rna" + extension

with open(txt_name, 'r') as read:
    s = read.readlines()[0]

s = s.replace("T", "U")

print(s)