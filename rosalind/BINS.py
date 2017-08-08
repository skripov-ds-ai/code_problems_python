import for_input_and_output

name = "bins"

file = for_input_and_output.read_file(name)

print(file)
print(file[2])
print(file[3])

n, m = int(file[0]), int(file[1])

a = [int(x) for x in file[2].split()]
k = [int(x) for x in file[3].split()]

s = ""

for ki in k:
    left, right = 0, n - 1
    middle = left + (right - left) // 2
    while left <= right:
        middle = left + (right - left) // 2
        if a[middle] == ki:
            break
        if a[middle] < ki:
            left = middle + 1
        else:
            right = middle - 1
    if a[middle] != ki:
        middle = -1
    else:
        middle += 1
    s += str(middle) + " "

s += '\n'

print()
print(s)

for_input_and_output.write_file(name, s)
