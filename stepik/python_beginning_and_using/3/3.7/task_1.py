from lxml import etree

parser = etree.XMLParser()
root = etree.fromstring(input().strip(), parser)


def dfs(v, colors, h=1):
    for vv in v.findall('cube'):
        dfs(vv, colors, h=h+1)
    colors[v.attrib['color']] += h


def traversal(root):
    colors = {
        'red': 0,
        'blue': 0,
        'green': 0,
    }

    dfs(root, colors)

    return colors


colors = traversal(root)

answ = ' '.join(map(str, [colors['red'], colors['green'], colors['blue']]))

print(answ)

