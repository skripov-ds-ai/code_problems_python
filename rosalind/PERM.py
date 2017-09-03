from itertools import permutations

import for_input_and_output

name = "perm"

file = [x.strip() for x in for_input_and_output.read_file(name)]


def all_permutations(n):
    res = []
    for permutation in permutations(range(1, n+1)):
        res.append(' '.join(map(str, permutation)))
    return res

p = all_permutations(int(file[0]))

s = str(len(p)) + "\n" + '\n'.join(map(str, p))

print(s)

for_input_and_output.write_file(name, s)
