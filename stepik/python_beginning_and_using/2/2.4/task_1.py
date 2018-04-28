with open('./input/data.txt', 'r') as r:
    with open('./output/result.txt', 'w') as w:
        w.writelines(r.readlines()[::-1])