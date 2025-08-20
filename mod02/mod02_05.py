luku1 = input("levisköjen lukumäärä: ") #8512grammaa
luku2 = input("naulojen lukumäärä: ") #425.6grammaa
luku3 = input("luotien lukumäärä: ") #13.3grammaa

#lukujen summa
summa = (int(luku1)*8512+int(luku2)*425.6+int(luku3)*13.3)
kokonaisosa = summa//1000
desimaaliosa = summa%1000

#grammojen pyöristäminen
pyoristys = round(desimaaliosa, 2)


print("Tulos nykymittojen mukaan: " + str(kokonaisosa) + "kg" + " ja " + str(pyoristys) + "g")

