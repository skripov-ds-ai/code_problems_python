import for_input_and_output

name = "revc"

file = [x.strip() for x in for_input_and_output.read_file(name)]

d = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A'
}

def add_space(s):
    return ' '.join(s)

def to_str(s):
    res = ''
    for x in s:
        res += str(x)
    return res

def my_replace(file, d):
    s = file[0]
    s1 = ''
    for i in range(len(s) - 1, -1, -1):
        s1 += d[s[i]]
    return s1

s = my_replace(file, d)

print(s)

for_input_and_output.write_file(name, s)