plaintext = input("plain text: ")
key = input("key: ")
cipher = ""
klen = len(key)
var = ""

for i in plaintext:
    if ord(i) >= 97 and ord(i) <= 122:
        var += i

for i in range(len(var)):
    c = ord(var[i]) + (ord(key[i%klen])-97)
    if c > 122:
        c = 96 + c % 122
    cipher += chr(c)

print("cipher text= "+cipher.upper())
