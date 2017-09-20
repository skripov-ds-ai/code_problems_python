import for_input_and_output

name = "dij"

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

for i in range(len(file)):
    file[i] = list(map(int, file[i]))

print(file)

graph = [[] for i in range(file[0][0])]
for i in range(file[0][0]):
    for j in range(file[0][0]):
        graph[i].append(0)

print(graph)

start = 0


s = ''

print()
print(s)

for_input_and_output.write_file(name, s)
