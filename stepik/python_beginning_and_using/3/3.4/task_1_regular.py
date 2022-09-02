from urllib.request import urlopen
import re

a, b = input().strip(), input().strip()
html1 = urlopen(a).read().decode('utf8').strip()

result = False

refs = lambda html: re.findall(r'a href="http.*"', html)
get_ref = lambda x: re.findall(r'http.*[^">]+', x)

refs1 = refs(html1)

for ref1 in refs1:
    try:
        html2 = urlopen(get_ref(ref1)[0]).read().decode('utf8').strip()

        refs2 = refs(html2)
        if b in [get_ref(x)[0] for x in refs2]:
            result = True
            break
    except:
        pass

res = lambda x: "Yes" if x else 'No'

print(res(result))