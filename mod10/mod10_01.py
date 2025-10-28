class Hissi:
    def __init__(self):
        self.kerros = 0
        self.ylin_kerros = 7
        self.alin_kerros = 0

    def siirry_kerrokseen(self, kerros):
        for k in range(kerros):
            self.kerros += 1




    def kerros_ylös(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1
        if self.kerros < 0:
            self.kerros = 0
        elif self.kerros > 7:
            self.kerros = self.ylin_kerros
        return self.kerros

hissi = Hissi()
hissi.siirry_kerrokseen(9)
hissi.kerros_ylös()
hissi.kerros_alas()

print(f"Hissin kerros on: {hissi.kerros}/{hissi.ylin_kerros}")


