table = []
plaintext = ""
key = ""
cipher = ""

for i in range(65, 91):
    plaintext += chr(i)
    key += chr(i)

for i in key:
    list = []
    for j in plaintext:
        c = ord(j) + (ord(i)-65)
        if c > 90:
            c = 64 + c % 90
        list.append(chr(c))
    table.append(list)

for i in table:
    print(i)

