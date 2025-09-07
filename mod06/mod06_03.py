def muunnin():
    while True:
        gallons = input("Anna bensiinin määrä (Nestegallonoina): ")
        tulos = float(int(gallons) * 3.785)
        print(tulos)
        if gallons < str(0):
            return

muunnin()
