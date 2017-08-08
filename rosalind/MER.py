import for_input_and_output

def min1(a, b):
    return a if a < b else b


def merge(a, b):
    c = []
    i1 = 0
    i2 = 0
    length = min1(len(a), len(b))
    while i1 < len(a) and i2 < len(b):
        if a[i1] < b[i2]:
            c.append(a[i1])
            i1 += 1
        else:
            c.append(b[i2])
            i2 += 1
    for i in range(i1, len(a)):
        c.append(a[i])
    for i in range(i2, len(b)):
        c.append(b[i])
    return c


name = "mer"

file = for_input_and_output.read_file(name)

a = [int(x) for x in file[1].split()]

print("a:")
print(a)

b = [int(x) for x in file[3].split()]

print("b:")
print(b)

s = ""

c = merge(a, b)


def print_array(array):
    s = ''
    for i in range(len(array)):
        s += str(array[i]) + " "
    s += "\n"
    return s


s = print_array(c)

print(s)

for_input_and_output.write_file(name, s)
