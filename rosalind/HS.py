import for_input_and_output

name = "hs"

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

print(file)

arr = [int(x) for x in file[1]]

def max_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):

    n = len(arr)

    for i in range(n // 2, -1, -1):
        max_heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


heap_sort(arr)

print(arr)

s = " ".join(map(str, arr))

print(s)

for_input_and_output.write_file(name, s)
