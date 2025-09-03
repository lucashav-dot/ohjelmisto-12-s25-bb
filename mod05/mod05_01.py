import random
lkm = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(lkm):
    heitto = random.randint(1, 6)
    summa += heitto
print(f"Silmälukujen summa on {summa}")