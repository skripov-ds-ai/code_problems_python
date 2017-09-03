import for_input_and_output

name = str(str(__file__).lower().split('/')[-1]).split('.')[0]

print(name)

file = [x.strip().split() for x in for_input_and_output.read_file(name)]

for i in range(len(file)):
    file[i] = [int(x) for x in file[i]]

k, n = file[0][0], file[0][1]

print(k, n)


class Pair:
    def __init__(self, index, x):
        self.index = index
        self.x = x

    def get_x(self):
        return self.x

    def get_index(self):
        return self.index

    def set_x(self, x):
        self.x = x

    def set_index(self, index):
        self.index = index

    def __str__(self):
        return str("{" + "index = {}; x = {}".format(self.index, self.x) + "}")

def sort_by_key(x):
    return abs(x.get_x())

index = 2
arr = []
for i in range(len(file[index])):
    arr += [Pair(i, file[index][i])]

arr.sort(key=sort_by_key)

print(arr[0])

ss = "["
for i in range(len(arr)):
    ss += str(arr[i])
    if i != len(arr) - 1:
        ss += ", "
ss += "]"
print(ss)

s = ''


for_input_and_output.write_file(name, s)
