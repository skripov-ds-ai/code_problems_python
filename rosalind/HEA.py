import for_input_and_output

name = "hea"

file = [x.strip() for x in for_input_and_output.read_file(name)]


s = ""

arr = [int(x) for x in file[1].split()]


def max_heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)

# if you want to use python libraries:
#
# import heapq
#
# (heapq._heapify_max(arr))


build_max_heap(arr)

s = ' '.join(map(str, arr))

print(s)

for_input_and_output.write_file(name, s)
