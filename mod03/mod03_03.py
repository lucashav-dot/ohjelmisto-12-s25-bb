puoli = input("Kerro Biologinen sukupuolesi (Nainen/Mies): ")
if puoli=="Nainen":
    hg = (input("Anna hemoglobiiniarvosi (g/l): ")) #Nainen 117-175 g/l.

    if hg<=str(116):
        print("Hemoglobiiniarvosi on Alhainen.")
    elif str(117)<=hg<=str(175):
        print("Hemoglobiiniarvosi on Normaali.")
    elif hg>=str(176):
        print("Hemoglobiiniarvosi on Korkea.")

if puoli=="Mies":
    hg2 = (input("Anna hemoglobiiniarvosi (g/l): ")) #mies 134-195 g/l.

    if hg2<=str(133):
        print("Hemoglobiiniarvosi on Alhainen.")
    elif str(134)<=hg2<=str(195):
        print("Hemoglobiiniarvosi on Normaali.")
    elif hg2>=str(196):
        print("Hemoglobiiniarvosi on Korkea.")
