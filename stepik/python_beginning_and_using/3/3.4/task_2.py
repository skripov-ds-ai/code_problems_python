import requests
import re

link = input()
response = requests.get(link)
data = response.text

r = re.compile(r'<a.*href\s*=\s*[\'\"](?:\w*p\w?://|../|/)?(([^\s\.\/]+\.[^:/\'\"]+)+).*[\'\"]')

result = sorted(set([x[0] for x in re.findall(r, data)]))

print('\n'.join(result))

