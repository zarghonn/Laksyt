import random

luku = random.randint(1, 10)
arvaus = int(input("arvaa luku:"))

while arvaus != luku:
    if arvaus < luku:
        print("liian pieni")
    else:
        print("liian suuri")

    arvaus = int(input("arvaa luku:"))

print("oikein")
