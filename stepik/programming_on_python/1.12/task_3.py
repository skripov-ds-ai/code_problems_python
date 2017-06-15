import sys
import math

a = float(input())
b = float(input())
op = input()

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y:  x / y if y != 0 else 'Деление на 0!',
    'div': lambda x, y: x // y if y != 0 else 'Деление на 0!',
    'mod': lambda x, y: x % y if y != 0 else 'Деление на 0!',
    'pow': lambda x, y: x ** y
}

print(operations[op](a, b))