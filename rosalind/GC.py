# todo!!

import for_input_and_output

name = "gc"

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

print(file)

strands = dict()

print("gc".count('c'))


name_gc = ''
for i in range(len(file)):
    #print(file[i][0])
    #print(file[i][0].startswith('>'))
    if file[i][0].startswith('>'):
        name_gc = file[i][0][1::]
    else:
        if name_gc in strands:
            strands[name_gc] += file[i][0]
        else:
            strands[name_gc] = file[i][0]

print(strands)

d = {}
gc = ['C', 'G']
for x in strands:
    d[x] = 0.0
    for i in gc:
        d[x] += strands[x].count(i)
    d[x] /= len(strands[x])

print(d)

a = sorted(d.items(), key=lambda x: x[1], reverse=True)

print(a[0])

s = '\n'.join(map(str, a[0]))

print()
print(s)

for_input_and_output.write_file(name, s)
