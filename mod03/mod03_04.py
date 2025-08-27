vuosi: str = input("Anna vuosiluku: ")
karkausvuosi = int(vuosi)/4 or int(vuosi)/400
if karkausvuosi in range(0,40000,4)or(karkausvuosi in range(0,40000,400)):
    print("vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")