import sys
import math

# dataset_3363_3
name = input().strip() + ".txt"

lines = ''

with open(name, 'r') as r:
    for line in r:
        lines += line.strip() + " "

string = [i.lower() for i in lines.split()]

from collections import Counter

result = Counter(string).most_common(1)[0]

#print(result)

output = "output_2.txt"

with open(output, 'w') as out:
    out.write("{} {}\n".format(result[0], result[1]))
