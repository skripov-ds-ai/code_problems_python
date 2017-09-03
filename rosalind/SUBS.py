import for_input_and_output

name = "subs"

file = [x.strip() for x in for_input_and_output.read_file(name)]


def find_all_occurrences_of_substring(s, t):
    return [(i + 1) for i in range(len(s)) if s.startswith(t, i)]


s = ' '.join(map(str, find_all_occurrences_of_substring(file[0], file[1])))

print(s)

for_input_and_output.write_file(name, s)
