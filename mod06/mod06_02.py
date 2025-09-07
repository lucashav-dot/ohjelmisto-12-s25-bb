import random
Num2=input("Anna nopan tahkojen lukumäärä: ")
num2 = int(Num2)
def noppa():
    return random.randint(1,num2 )

def paaohjelma():
    num = 0
    while num != num2:
        num=noppa()
        print(num)


paaohjelma()