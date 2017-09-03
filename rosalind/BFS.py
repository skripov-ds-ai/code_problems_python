import for_input_and_output

name = "bfs"

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

for i in range(len(file)):
    file[i] = list(map(int, file[i]))

print(file)

graph = [[] for i in range(file[0][0])]
for i in range(file[0][1]):
    graph[file[i + 1][0] - 1].append(file[i + 1][1] - 1)

print(graph)

start = 0

def bfs(start, graph):
    dist = [-1 for i in range(len(graph))]

    dist[start] = 0

    queue = []
    visited = [False] * (len(graph))

    queue.append(start)
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        # print("vertex =", vertex)
        for i in graph[vertex]:
            # print("i =", i)
            if not visited[i]:
                queue.append(i)
                dist[i] = dist[vertex] + 1
                visited[i] = True

    return dist


distances = bfs(start, graph)

s = ' '.join(map(str, distances))

print(s)

for_input_and_output.write_file(name, s)
