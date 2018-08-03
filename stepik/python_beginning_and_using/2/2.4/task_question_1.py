import os
import zipfile
from sortedcontainers import SortedSet
from urllib.request import urlopen

path = 'z.zip'
path1 = './z'


def names_of_pyfiles(root):
    paths = []
    pattern = '.py'

    for path, subdirs, files in os.walk(root):
        for file in files:
            if file[-3:] == pattern:
                paths.append(path[4:])

    return '\n'.join(SortedSet(paths))

url = 'https://stepik.org/media/attachments/lesson/24465/main.zip'
resp = urlopen(url)

data = resp.read()
with open(path, "wb") as z:
    z.write(data)

z = zipfile.ZipFile(path, 'r')
z.extractall(path1)
z.close()

print(names_of_pyfiles(path1))