import json

js = json.loads(input())

d = {}
for j in js:
    class_name = j['name']
    parents = j['parents']
    if class_name not in d:
        d[class_name] = []
    for cl1 in parents:
        if cl1 not in d:
            d[cl1] = [class_name]
        else:
            d[cl1].append(class_name)

dt = {}
for k in d:
    dt[k] = set(d[k])
del d
d = dt


def dfs_helper(v, visited, d, tmp):
    visited[v] = True
    if v not in d:
        return tmp

    tmp |= d[v]

    for k in d[v]:
        if not visited[k]:
            tmp |= dfs_helper(k, visited, d, tmp=tmp)

    return tmp


def dfs(d, k):
    all_vertex = set([x for x in d] + [y for x in d for y in d[x]])
    visited = {x: False for x in all_vertex}
    return dfs_helper(k, visited, d, tmp=set())

answ = sorted([(k, dfs(d, k)) for k in d], key=lambda x: x[0])
answ = [x[0] + " : " + str(len(x[1]) + 1) for x in answ]
answ = '\n'.join(answ)

print(answ)

