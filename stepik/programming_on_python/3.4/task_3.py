import sys

n = 3

subjects = []

default = 0.0

for i in range(n):
    subjects += [default]

count = 0

delimiter = ';'

# dataset_3363_4
name = "dataset_3363_4.txt"
#name = input().strip() + ".txt"

with open(name, 'r') as my_input:
    for line in my_input:
        count += 1

        line = line.strip().split(delimiter)

        line.remove(line[0])

        med = 0.0
        for i in range(len(line)):
            med += int(line[i])
            subjects[i] += int(line[i])
        med /= len(line)

        print(med)

for i in range(len(subjects)):
    subjects[i] /= count
    sys.stdout.write("{} ".format(subjects[i]))

print()