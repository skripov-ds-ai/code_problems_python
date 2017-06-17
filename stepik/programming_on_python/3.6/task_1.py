import sys
import requests as rq

name = 'dataset_3378_2.txt'
# name = input().strip() + ".txt"

with open(name, 'r') as dt:
    s = dt.read()

file = rq.get(s.strip())

delimiter = '\n'

print(file.text.count(delimiter))
