kala = float(input("Kuinka pitkä kalasi on? "))
if kala >= 37:
    print("Kalasi on tarpeeksi pitkä")

elif kala <= 36:
    lyhyt = int(37) - kala
    print("kalasi on " + str(lyhyt) + "cm liian lyhty")
