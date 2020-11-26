cipher = input("cipher text: ")
key = input("key: ")
plaintext = ""
klen = len(key)
var = cipher.lower()

for i in range(len(var)):
    c = ord(var[i]) - (ord(key[i%klen])-97)
    if c < 97:
        c = 122 - (96 - c)
    plaintext += chr(c)

print(plaintext)
