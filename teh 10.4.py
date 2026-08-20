import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi}")
        print("-" * 65)
        print(f"{'Rekisteritunnus':<20}{'Nopeus':>10}{'Matka':>15}")
        print("-" * 65)

        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<20}"
                f"{auto.nopeus:>10} km/h"
                f"{auto.matka:>12.1f} km"
            )

        print("-" * 65)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True

        return False


# Pääohjelma

autot = []

for i in range(10):
    auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        print(f"\nKilpailua kulunut {tunti} tuntia.")
        kilpailu.tulosta_tilanne()

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!")
kilpailu.tulosta_tilanne()