import for_input_and_output

# >= len // 2
def major_element1(arr):
    index = 0
    count = 0
    for i in range(len(arr)):
        if count == 0:
            index = i
            count += 1
        elif a[index] == a[i]:
            count += 1
        else:
            count -= 1
    return a[index] if count > 0 else -1

# > len // 2
def major_element2(arr):
    index = 0
    count = 1
    for i in range(len(arr)):
        if a[index] == a[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1
        # print("x = {}; count = {}".format(a[index], count))
    return a[index] if count > 1 else -1


name = "maj"

file = for_input_and_output.read_file(name)

# print(file)

q1 = [int(x) for x in file[0].split()]

k, n = q1[0], q1[1]

s = ""

for i in range(0, k):
    # print(i)
    # print(file[i])
    # print(file[i + 1])
    a = [int(x) for x in file[i + 1].split()]
    s += str(major_element2(a)) + " "

s += "\n"

for_input_and_output.write_file(name, s)
