import sys
import math

extension = '.txt'
directory = './input/'
name_part = 'rosalind_'
problem_name = 'ins'
txt_name = directory + name_part + problem_name + extension

new_line = '\n'
space = ' '


def insertion_sort1(array):
    count = 0
    for i in range(1, len(array)):
        t = array[i]
        j = i - 1
        while j >= 0 and t < array[j]:
            array[j + 1] = array[j]
            j -= 1
            count += 1
        array[j + 1] = t
        count += 1
    return count


def insertion_sort2(array):
    count = 0
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
            count += 1
    return count


def print_array(array):
    s = ''
    for i in range(len(array)):
        s += str(array[i]) + space
    s += new_line
    print(s)


with open(txt_name, 'r') as read:
    input_str = read.readlines()

n = int(input_str[0])



arr = [int(x) for x in input_str[1].split()]

# print(input_str[1])

# print(arr)

# print(n)
# print(len(arr))

count = insertion_sort2(arr)
print(count)
print_array(arr)