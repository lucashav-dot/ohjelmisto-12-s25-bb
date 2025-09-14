lentokentta = {}

while True:
    komento = input("Haluatko LISÄTÄ vai HAKEA lentokenttää.(paina Enter lopettaaksesi): ")
    if komento == "lisätä":
        icao=input("Anna lentokentän ICAO-koodi: ")
        nimi=input("Anna lentokentän nimi: ")
        if icao in lentokentta:
            print("lentokenttä on jo lisätty hakemistoon")
        lentokentta[icao] = nimi
    if komento == "etsiä":
        koodi=input("Anna lentoketän ICAO-koodi: ")
        if koodi in lentokentta:
            print(lentokentta[koodi])
        else:
            print("Virheellinen ICAO-koodi")
    if komento == "lopeta":
        break


