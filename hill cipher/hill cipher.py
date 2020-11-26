n = int(input("enter dimension for key matrix:"))
key = input("enter key(capitals): ")
plaintext = input("enter plain text(small): ")
text = plaintext.upper()
kmat = []

for i in range(0, n):
    list = []
    for j in range(0, n):
        list.append(ord(key[n*i+j])-65)
    kmat.append(list)

for i in kmat:
    print(i)

addlen = len(text) % n
for i in range(addlen):
    text += 'x'

cipher = []

for i in range(0, len(text), n):
    for j in range(0, n):
        sum = 0
        for k in range(0, n):
            sum += kmat[j][k]*(ord(text[i+k])-65)
        mod = sum % 26
        cipher.append(mod)

print("cipher text :")
for i in cipher:
    print(chr(i+65), end='')
