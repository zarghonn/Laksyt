luvut = []

luku = input("anna luku")

while luku != "":
    luku = input("anna luku")
    luvut.append(int(luku))

luvut.sort(reverse=True)
print(luvut[5:])