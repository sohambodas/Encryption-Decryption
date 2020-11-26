mat = []
key = input("key: ")
key = key.replace('j', 'i')
key2 = ""

for i in key:
    if i not in key2:
        key2 += i
key2 = key2.upper()

for i in range(65, 91):

    if (chr(i) not in key2) and (chr(i) != 'J'):
        key2 += chr(i)

print("final key: "+key2)

for i in range(0, 5):
    list = []
    for j in range(0, 5):
        list.append(key2[5*i+j])
    mat.append(list)

for i in mat:
    print(i)

text = input("encrypted text: ")
cipher = ""

for i in range(0, len(text), 2):
    r1, c1, r2, c2 = 0, 0, 0, 0
    for j in range(0, 5):
        for k in range(0, 5):
            if text[i] == mat[j][k]:
                r1 = j
                c1 = k
            if text[i+1] == mat[j][k]:
                r2 = j
                c2 = k
    if r1 == r2:
        cipher += mat[r1][(c1-1) % 5]
        cipher += mat[r2][(c2-1) % 5]
    elif c1 == c2:
        cipher += mat[(r1-1) % 5][c1]
        cipher += mat[(r2-1) % 5][c2]
    else:
        cipher += mat[r1][c2]
        cipher += mat[r2][c1]

print("cipher text: ", cipher.lower())


