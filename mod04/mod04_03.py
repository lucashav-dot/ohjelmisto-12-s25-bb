luvut = []

while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    try:
        luku = float(luku)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte.")
if luvut:
    suurin = max(luvut)
    pienin = min(luvut)
    print(f"Isoin luku on: {suurin}")
    print(f"Pienin luku on: {pienin}")
else:
    print("Et syöttänyt yhtään lukua.")
