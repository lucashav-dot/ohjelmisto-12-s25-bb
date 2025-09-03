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
luvut.sort(reverse=True)
print(luvut[:5])