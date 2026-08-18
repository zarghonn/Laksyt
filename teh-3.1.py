pituus = float(input("kuhan pituus : "))

if pituus < 37:

    #kuha on alamittainen. Lasketaan kuinka paljon.
    alamisttaisuus = 37 - pituus
    print(f"kalasi on {alamisttaisuus}.cm liian lyhyt!")

else:
    print("voit syödä kalan")