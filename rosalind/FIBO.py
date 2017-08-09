import for_input_and_output


mem = dict()

def _fib(n):
    if n == 0:
        return 0, 1

    if n == 1:
        return 1, 1

    if n in mem:
        return mem[n]

    a, b = _fib(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b

    ans1, ans2 = 0, 0

    if n % 2 == 0:
        ans1, ans2 = c, d
    else:
        ans1, ans2 = d, c + d

    mem[n] = ans1
    mem[n // 2 + 1] = ans2

    return ans1, ans2


def fib(n):
    f = _fib(abs(n))
    if n < 0 and abs(n) % 2 != 0:
        f *= -1
    return f[0]


name = "fibo"

file = [x.strip() for x in for_input_and_output.read_file(name)]

a = [int(x) for x in file[0].split()]

print(a[0])
print()

s = str(fib(a[0]))

print(s)

for_input_and_output.write_file(name, s)
