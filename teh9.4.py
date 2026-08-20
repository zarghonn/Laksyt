
import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# Pääohjelma
autot = []

# Luodaan 10 autoa
for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

# Kilpailu alkaa
while not any(auto.kuljettu_matka >= 10000 for auto in autot):
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

# Tulostetaan tulokset
print(f"{'Rekisteri':<12}{'Huippunopeus':<16}"
      f"{'Nopeus':<12}{'Kuljettu matka':<16}")
print("-" * 56)

for auto in autot:
    print(f"{auto.rekisteritunnus:<12}"
          f"{auto.huippunopeus:<16}"
          f"{auto.nopeus:<12}"
          f"{auto.kuljettu_matka:<16.1f}")
