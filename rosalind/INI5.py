import for_input_and_output
import sys
import math

name = "ini5"

file = for_input_and_output.read_file(name)

out_s = ''

for i in range(1, len(file), 2):
    out_s += file[i]

print(out_s)

for_input_and_output.write_file(name, out_s)
