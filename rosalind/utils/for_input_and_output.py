import sys

from Bio import SeqIO

extension = '.txt'
directory_input = './input/'
directory_output = './output/'
name_part = 'rosalind_'
out = "out_"

def read_file(problem_name):
    txt_name = directory_input + name_part + problem_name + extension
    with open(txt_name, 'r') as read:
        arr = read.readlines()
    return arr

def read_seq(problem_name, method):
    txt_name = directory_input + name_part + problem_name + extension
    with open(txt_name, 'r') as r:
        seq = SeqIO.read(r, method)
    return seq


def write_file(output_name, s):
    txt_name = directory_output + name_part + out + output_name + extension
    with open(txt_name, 'w') as write:
        write.write(s)
