import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
problem_name = 'iprb'
txt_name = directory + name_part + problem_name + extension

with open(txt_name, 'r') as read:
    input_str = [int(x) for x in read.readlines()[0].split()]

k, m, n = input_str[0], input_str[1], input_str[2]

print(k, m, n)


def mendel_first(k, m, n):
    population = k + m + n

    def f(a, b = population):
        return a / b / (b - 1)

    dom1 = k / population

    het1dom2 = f(m * k)
    het1het2 = f(m * (m - 1) * 3) / 4
    het1rec2 = f(m * n) / 2

    het1 = het1dom2 + het1het2 + het1rec2

    rec1dom2 = f(n * k)
    rec1het2 = f(n * m) / 2

    rec1 = rec1dom2 + rec1het2

    return dom1 + het1 + rec1


s = ''

s += str(mendel_first(k, m, n))

print(s)
