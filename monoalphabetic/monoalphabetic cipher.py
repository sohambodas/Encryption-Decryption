var = input("text: ")
key = input("key: ")
var1 = ""
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
    if ord(i) >= 97 and ord(i) <= 122:
        var1 += i

for i in var1:

    var2 += key2[ord(i)-97]

print("encrypted text: "+var2.upper())

