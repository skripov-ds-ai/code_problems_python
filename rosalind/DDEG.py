import for_input_and_output

name = "ddeg"

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
    s = []
    for i in g:
        s += [(len(i))]
    return s


degs = degrees(g)

print(degs)


def double_degree(g):
    s = []
    for i in range(len(g)):
        t = 0
        for j in g[i]:
            t += len(g[j])
        s += [t]
    return s


ddegs = double_degree(g)

print(ddegs)

s = ""


def to_str(a):
    s = ''
    for i in a:
        s += str(i) + " "
    s += '\n'
    return s


s += to_str(ddegs)

print(s)

for_input_and_output.write_file(name, s)
