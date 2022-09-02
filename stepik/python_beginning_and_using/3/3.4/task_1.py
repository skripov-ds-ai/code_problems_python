from urllib.request import urlopen
from bs4 import BeautifulSoup # bs4 is not on this step :(

a, b = input().strip(), input().strip()
soup = BeautifulSoup(urlopen(a).read().decode('utf8').strip())

result = False

for link in soup.findAll('a'):
    ref = link.get('href')
    c = BeautifulSoup(urlopen(ref).read().decode('utf8').strip())
    refs = []
    for link1 in soup.findAll('a'):
        ref1 = link.get('href')
        refs.append(ref1)
    if b in refs:
        result = True
        break

print('Yes' if result else 'No')

