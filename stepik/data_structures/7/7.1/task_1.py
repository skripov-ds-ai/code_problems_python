a = input()


def encodeString(message):
    return ' '.join([str(int(x)) for x in message.encode('ascii')])


print(encodeString(a))
print(*a.encode('ascii'))