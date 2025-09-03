

luku = int(input("Anna luku: "))
alkuluku = True
for i in range(2, int(luku**0.5)+1):
    if luku % i == 0:
        alkuluku = False
        print(f"{luku} ei ole alkuluku")
        break
if alkuluku:
    print (f"{luku} on alkaluku")