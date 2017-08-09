import for_input_and_output


count = 0


def min1(a, b):
    return a if a < b else b


def merge(a, b):
    c = []
    i1 = 0
    i2 = 0
    count = 0
    # length = min1(len(a), len(b))
    while i1 < len(a) and i2 < len(b):
        if a[i1] <= b[i2]:
            c.append(a[i1])
            i1 += 1
        else:
            c.append(b[i2])
            i2 += 1
            count += (len(a) - i1)
    for i in range(i1, len(a)):
        c.append(a[i])
    for i in range(i2, len(b)):
        c.append(b[i])
    return c, count


def merge_sort(arr):
    count = 0
    if len(arr) < 2:
        return arr, count

    middle = len(arr) // 2

    left, count1 = merge_sort(arr[:middle])
    right, count2 = merge_sort(arr[middle:])

    c, count3 = merge(left, right)

    count = count1 + count2 + count3

    return c, count


name = "inv"

file = for_input_and_output.read_file(name)

a = [int(x) for x in file[1].split()]

print("a:")
print(a)

s = ""

c, count = merge_sort(a)


def print_array(array):
    s = ''
    for i in range(len(array)):
        s += str(array[i]) + " "
    s += "\n"
    return s


s = print_array(c)

print(s)
print("count = {}".format(count))

for_input_and_output.write_file(name, s)