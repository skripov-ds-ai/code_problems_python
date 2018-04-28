from simplecrypt import encrypt, decrypt

with open("./input/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)

with open("./input/passwords.txt", "rb") as inp:
    passwords = [x.strip() for x in inp.readlines()]
    print(passwords)

for password in passwords:
    try:
        print("password =", password)
        print(decrypt(password, encrypted))
    except Exception:
        print("Exception :(")
    print()