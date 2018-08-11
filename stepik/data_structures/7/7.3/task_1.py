def counts(a):
    out = [0]*256
    for i in range(len(a)):
        out[ord(a[i])] += 1
    return out


print(counts(input()))

