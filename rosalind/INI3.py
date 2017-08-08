import for_input_and_output
import sys
import math


file = for_input_and_output.read_file("ini3")

# print(file)

s = file[0]
s1 = [int(x) for x in file[1].split()]
a, b, c, d = s1[0], s1[1], s1[2], s1[3]

print("{} {}".format(s[a:(b + 1)], s[c:(d + 1)]))
