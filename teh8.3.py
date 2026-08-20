import sqlite3
from geopy.distance import geodesic

yhteys = sqlite3.connect("airports.db")
kursori = yhteys.cursor()

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

sql = """
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident = ?
"""

kursori.execute(sql, (icao1.upper(),))
lentokentta1 = kursori.fetchone()

kursori.execute(sql, (icao2.upper(),))
lentokentta2 = kursori.fetchone()

if lentokentta1 and lentokentta2:
    koordinaatit1 = (lentokentta1[0], lentokentta1[1])
    koordinaatit2 = (lentokentta2[0], lentokentta2[1])

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"Lentokenttien välinen etäisyys on {etaisyys:.1f} kilometriä.")
else:
    print("Jompaakumpaa lentokenttää ei löytynyt.")

yhteys.close()