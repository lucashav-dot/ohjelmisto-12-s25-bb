class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylin_kerros or kerros < self.alin_kerros:
            print(f"Kerrosta {kerros} ei ole olemassa ({self.alin_kerros}-{self.ylin_kerros})")
            return

        while self.kerros < kerros:
            self.kerros_ylös()
        while self.kerros > kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissi_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissi_lkm)]

    def aja_hissiä(self, hissin_numero, kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero} kerrokseen {kerros}")
            self.hissit[hissin_numero].siirry_kerrokseen(kerros)
        else:
            print("Virhe: hissiä ei ole olemassa.")



talo = Talo(0, 7, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 2)




hissi = Hissi(0, 7)
hissi.siirry_kerrokseen(9)
hissi.kerros_ylös()
hissi.kerros_alas()

print(f"Hissin kerros on: {hissi.kerros}/{hissi.ylin_kerros}")