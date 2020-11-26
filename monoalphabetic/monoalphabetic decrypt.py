var = input("plain text: ")
key = input("key: ")
var2 = ""
key2 = ""

for i in key:
    if i not in key2:
        key2 += i
key2 = key2.upper()

for i in range(65, 91):

    if chr(i) not in key2:
        key2 += chr(i)

print("final key: "+key2)

for i in var:
    for j in range(0, 25):
        if i == key2[j]:
            var2 += chr(97+j)
            break


print("plain text: "+var2)

