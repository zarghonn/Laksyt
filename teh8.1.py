import sqlite3

yhteys = sqlite3.connect("airports.db")
kursori = yhteys.cursor()

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = """
SELECT name, municipality
FROM airport
WHERE ident = ?
"""

kursori.execute(sql, (icao,))
tulos = kursori.fetchone()

if tulos:
    print(f"Lentoasema: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentoasemaa ei löytynyt.")

yhteys.close()