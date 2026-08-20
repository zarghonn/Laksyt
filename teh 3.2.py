hyttiluokka = input("Anna hyttiluokka: ")

if hyttiluokka == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")