import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
problem_name = 'iprb'
txt_name = directory + name_part + problem_name + extension

with open(txt_name, 'r') as read:
    input_str = read.readlines()

k, m, n = input_str[0], input_str[1], input_str[2]
