oikea_salasana = "rules"
tunnus = "python"
toistojen_lkm=4
i=0

while True:
    input_tunnus = input("Käyttäjätunnus: ")
    input_salasana = input("Anna salasana: ")
    i += 1
    if i > toistojen_lkm:
        print("liian monta yritystä, yritä myöhemmin uudestaan")
        break
    elif input_salasana != oikea_salasana or input_tunnus != tunnus:
        print("pääsy evätty")

    elif input_salasana == oikea_salasana and input_tunnus == tunnus:
        print("Tervetuloa")
        break