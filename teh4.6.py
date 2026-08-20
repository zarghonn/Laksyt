import random

määrä = int(input("Montako pistettä arvotaan: "))

sisällä = 0
laskuri = 0

while laskuri < määrä:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        sisällä += 1

    laskuri += 1

pi = 4 * sisällä / määrä

print("Piin likiarvo:", pi)