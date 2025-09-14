kuukausi = {
    1: 'Tammikuu', 2: 'Helmikuu', 3: 'Maaliskuu',
    4: 'Huhtikuu', 5: 'Toukokuu', 6: 'Kesäkuu',
    7: 'Heinäkuu', 8: 'Elokuu', 9: 'Syyskuu',
    10: 'Lokakuu', 11: 'Marraskuu', 12: 'Joulukuu'
}

kuu = int(input("Anna kuukausi lukuna (1–12): "))
if kuu in kuukausi:
    if kuu in (12, 1, 2):
        print(f"{kuukausi[kuu]} on Talvi kuukausi.")
    elif kuu in (3, 4, 5):
        print(f"{kuukausi[kuu]} on Kevät kuukausi.")
    elif kuu in (6, 7, 8):
        print(f"{kuukausi[kuu]} on Kesä kuukausi.")
    elif kuu in (9, 10, 11):
        print(f"{kuukausi[kuu]} on Syys kuukausi.")
else:
    print("Anna luku välillä 1–12.")
