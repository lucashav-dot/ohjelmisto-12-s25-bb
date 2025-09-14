nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi in nimet:
        print(f"{nimi} on jo lisätty listaan")
    else:
        print(f"{nimi} lisätty listaan")
    nimet.add(nimi)
    if nimi == "":
        break
for n in nimet:
    print(n)
