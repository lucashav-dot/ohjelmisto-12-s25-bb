import math

def yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * sade_m**2
    yksikkohinta = hinta_euro / pinta_ala
    return yksikkohinta

def main():
    print("Syötä ensimmäisen pizzan tiedot:")
    halkaisija1 = float(input("Halkaisija: "))
    hinta1 = float(input("Hinta: "))

    print("\nSyötä toisen pizzan tiedot:")
    halkaisija2 = float(input("Halkaisija: "))
    hinta2 = float(input("Hinta: "))

    yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

    print(f"\nPizza 1 yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"Pizza 2 yksikköhinta: {yksikkohinta2:.2f} €/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("Pizza 1 antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Pizza 2 antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat tarjoavat saman vastineen rahalle.")

main()
