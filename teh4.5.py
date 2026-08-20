oikea_salasana = "rules"
oikea_käyttäjätunnus = "python"
yritykset = 0

while yritykset < 5:
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset = yritykset + 1
    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa")
