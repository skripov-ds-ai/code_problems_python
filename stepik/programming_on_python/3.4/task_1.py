import sys
import math

name = input().strip() + ".txt"

# dataset_3363_2

with open(name, 'r') as r:
    s = r.readline().strip()

length = len(s)
i = 0
char = ' '
count = ""

res = ""

while i < length:
    if s[i].isalpha():
        char = s[i]
        i += 1
        count = ""
    else:
        while i < length and s[i].isdigit():
            count += s[i]
            i += 1
        res += char * int(count)

res += '\n'

output = "output_1.txt"

with open(output, 'w') as out:
    out.write(res)
