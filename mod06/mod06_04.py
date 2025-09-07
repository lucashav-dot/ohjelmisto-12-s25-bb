def laskin():
    luvut = []
    while True:
        luku = input("Anna luku: ")
        if luku == "":
            print("Lukujen summa on:", sum(luvut))
            break
        luvut.append(float(luku))
laskin()