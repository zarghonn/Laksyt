import random

määrä = int(input("Montako arpakuutiot: "))

summa = 0
for i in range(määrä):
     silmäluku= random.randint(1,6)
     summa += silmäluku

print("silmälukujen summa:",summa)
