d = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}

encode = lambda s: ''.join(map(lambda x: d[x], s))

a = input()

print(encode(a))
print(*map(lambda x: d[x], a), sep='')

