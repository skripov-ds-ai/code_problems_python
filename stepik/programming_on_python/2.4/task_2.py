import sys
import math

s = input() + " "
ss = ""

counter = 1

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
    else:
        ss = ss + s[i] + str(counter)
        counter = 1

print(ss)

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'

print(students)

a = [1, 2, 3]
b = a
# значения списка b?

a[1] = 10
# значения списка b?

b[0] = 20
# значения списка a?

a = [5, 6]
# значения списка b?

print(a)
print(b)