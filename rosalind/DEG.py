import for_input_and_output

name = "deg"

file = [x.strip() for x in for_input_and_output.read_file(name)]

inputs = []

for i in range(len(file)):
    inputs += [[int(x) for x in file[i].split()]]

print(inputs)

n, m = inputs[0][0], inputs[0][1]

g = []

for i in range(n):
    g += [[]]

for i in range(m):
    t = inputs[i + 1]
    g[t[0] - 1] += [t[1] - 1]
    g[t[1] - 1] += [t[0] - 1]

print(g)


def degrees(g):
    s = ''
    for i in g:
        s += str(len(i)) + " "
    return s

s = ""

s += degrees(g) + "\n"

print(s)

for_input_and_output.write_file(name, s)
