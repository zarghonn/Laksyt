import sqlite3

yhteys = sqlite3.connect("airports.db")
kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi: ")

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = ?
GROUP BY type
"""

kursori.execute(sql, (maakoodi.upper(),))

tulokset = kursori.fetchall()

for tyyppi, maara in tulokset:
    print(f"{tyyppi}: {maara}")

yhteys.close()