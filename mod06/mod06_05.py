def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]


def main():
    lista = []
    while True:
        lk = input("Anna luku: ")
        if lk == "":
            break
        luku = int(lk)
        lista.append(luku)

    karsittu_lista = poista_parittomat(lista)

    print("Alkuperäinen lista:", lista)
    print("Karsittu lista:", karsittu_lista)


main()