# todo
import for_input_and_output

name = "iev"

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

print(len(file))

s = str()

for_input_and_output.write_file(name, s)
