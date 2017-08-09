import for_input_and_output

name = "fibd"

file = [x.strip() for x in for_input_and_output.read_file(name)]

a = [int(x) for x in file[0].split()]


def fibd(n, m):
    generations = [0, 1, 1]
    it = 2
    while it < n:
        if it < m:
            generations.append(generations[-2] + generations[-1])
        elif it - m < 2:
            generations.append(generations[-2] + generations[-1] - 1)
        else:
            generations.append(generations[-2] + generations[-1] - generations[-m-1])
        it += 1
    print(generations)
    return generations[n]

print(a[0])
print(a[1])
print()

s = str(fibd(a[0], a[1]))

print(s)

for_input_and_output.write_file(name, s)
