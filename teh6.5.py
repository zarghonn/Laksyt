def karsi_parittomat(luvut):
    karsittu = []

    for luku in luvut:
        if luku % 2 == 0:
            karsittu.append(luku)

    return karsittu


# Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

karsittu = karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu)