import sys
import requests as rq

url = "https://stepic.org/media/attachments/course67/3.6.3/"

name = 'dataset_3378_3.txt'
# name = input().strip() + ".txt"

with open(name, 'r') as dt:
    s = dt.read()

file = rq.get(s.strip())

end = 'We'

counter = 1

while (file.text.strip().split(' '))[0] != end:
    counter += 1
    file = rq.get(url + file.text.strip())

print(counter)

del name
name = "result.txt"

with open(name, 'w') as w:
    w.write(file.text)
