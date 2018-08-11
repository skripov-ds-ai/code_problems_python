d = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}

a = input()

#res = ''
for i in range(len(a) // 2):
    print(d[a[2*i:2*(i + 1)]], end='')
    #res += d[a[2*i:2*(i + 1)]]
#print(res)
