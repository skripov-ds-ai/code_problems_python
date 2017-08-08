import sys
import math

extension = '.txt'
directory = './input/'
txt_name = directory + "rosalind_iprb" + extension

with open(txt_name, 'r') as read:
    input_str = read.readlines()

k, m, n = input_str[0], input_str[1], input_str[2]
