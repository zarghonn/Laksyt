luku = input("anna luku:")

if luku != "":
    luku = int(luku)
    pienin = luku
    suurin = luku

    while True:
        luku = input("anna luku:")
        if luku == "":
            break
        luku = int(luku)

        if luku > suurin:
            suurin = luku

    print("pienin:", pienin)
    print("suurin:", suurin)