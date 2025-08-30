import random

pisteet = input("Anna pisteiden määrä: ")
# kaikkien pisteiden määrä N
N = int(pisteet)
# ympyrän sisään osuvien pisteiden lkm n
n = 0
i = 0
while i < N:
    i = i + 1
    # arvotaan satunnainen piste koordinaatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    lasku = float(x**2 + y**2 < 1)
    if lasku == 1:
        n += 1
piin_likiarvo = float((4 * n)/N)
print(piin_likiarvo)
