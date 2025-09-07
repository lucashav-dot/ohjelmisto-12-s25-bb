import random

def noppa():
    return random.randint(1, 6)

def paaohjelma():
    num = 0
    while num != 6:
        num=noppa()
        print(num)


paaohjelma()