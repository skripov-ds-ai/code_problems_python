import for_input_and_output

name = "fib"

file = [x.strip() for x in for_input_and_output.read_file(name)]

a = [int(x) for x in file[0].split()]


def recurrent(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return recurrent(n - 1, k) + k * recurrent(n - 2, k)


def dynamic(n, k):
    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1

    for i in range(n):
        a, b = b, b + k * a

    return a


s = '' + str(dynamic(a[0], a[1]))

print(s)
print(recurrent(a[0], a[1]))

for_input_and_output.write_file(name, s)