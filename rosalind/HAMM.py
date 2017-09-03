import for_input_and_output

name = "hamm"

file = [x.strip() for x in for_input_and_output.read_file(name)]


def hemming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("len(s1)!=len(s2)")
    tmp = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            tmp += 1
    return tmp


s = str(hemming_distance(file[0], file[1]))

print(s)

for_input_and_output.write_file(name, s)
