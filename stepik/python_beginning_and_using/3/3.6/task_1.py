import requests

with open('dataset.txt') as f:
    s = f.readlines()

api_url = 'http://numbersapi.com/%d/math?json=true'
numbers = list(map(int, s))

for n in numbers:
    res = requests.get(api_url % n)
    if 'false' in res.text:
        print('Boring')
    else:
        print('Interesting')

