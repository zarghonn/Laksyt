
class Auto:
    def __init__(self, nopeus, kuljettu_matka=0):
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


auto = Auto(60, 2000)
auto.kulje(1.5)

print(auto.kuljettu_matka)
