import random

luku = random.randint(1, 10)
while True:
    arvaus = input("Arvaa luku (1-10): ")
    arvaus = int(arvaus)
    if arvaus > luku:
        print("liian suuri arvaus")
    elif arvaus < luku:
        print("liian pieni arvaus")
    elif arvaus == luku:
        print("oikein")
        break