import for_input_and_output

name = "ini6"

file = for_input_and_output.read_file(name)

arr = file[0].split()

print(arr)

dictionary = {}

for i in range(len(arr)):
    if arr[i] not in dictionary:
        dictionary[arr[i]] = 1
    else:
        dictionary[arr[i]] += 1

print(dictionary)

s = ''

for x in dictionary.items():
    s += str(x[0]) + " " + str(x[1]) + "\n"

print(s)

for_input_and_output.write_file(name, s)
