var = input("text: ")
key = int(input("key: "))
var1 = ""
var2 = ""

for i in var:
    if ord(i) >= 97 and ord(i) <= 122:
        var1 += i

for i in var1:
    j = ord(i) + key
    if j > 122:
        j = 96 + j % 122

    var2 += chr(j)

print(var2.upper())
