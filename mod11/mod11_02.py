class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankinkoko = tankinkoko


if __name__ == "__main__":
    sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdyta(120)
    polttomoottoriauto.kiihdyta(100)

    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauto {sahkoauto.rekisteritunnus}: {sahkoauto.matkamittari} km ajettu")
    print(f"Polttomoottoriauto {polttomoottoriauto.rekisteritunnus}: {polttomoottoriauto.matkamittari} km ajettu")
