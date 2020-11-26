var = input("text: ")
key = int(input("key: "))
var1 = ""
var2 = ""

for i in var:
    if ord(i) >= 65 and ord(i) <= 90:
        var1 += i

for i in var1:
    j = ord(i) - key
    if j < 65:
        j = 91 - (65-j)

    var2 += chr(j)

print(var2.lower())
