def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa += luku

    return summa


# Pääohjelma
luvut = [2, 5, 7, 10, 3]

summa = laske_summa(luvut)

print("Listan lukujen summa on:", summa)