import random

class Car:
    def __init__(self, number):
        self.speed = 80
        self.trip = 0
        self.top_speed = random.randint(100, 200)
        self.name = f"ABC-{number}"

    def accelerate(self):
        self.speed += random.randint(-10, 15)
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.top_speed:
            self.speed = self.top_speed

    def drive(self):
        self.trip += self.speed


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.accelerate()
            auto.drive()

    def tulosta_tilanne(self):
        print(f"\n{'Auto':<10}{'Huippu':<10}{'Nopeus':<10}{'Matka':<10}")
        print("-" * 40)
        for auto in self.autot:
            print(f"{auto.name:<10}{auto.top_speed:<10}{auto.speed:<10}{auto.trip:<10.1f}")
        print("-" * 40)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.trip >= self.pituus:
                return True
        return False

cars = [Car(i) for i in range(1, 11)]

kilpailu = Kilpailu("Suuri romuralli", 8000, cars)


tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"\n== Tilanne {tunti} tunnin jälkeen ==")
        kilpailu.tulosta_tilanne()

print("\nKilpailu on päättynyt! Lopputilanne:")
kilpailu.tulosta_tilanne()

voittaja = max(cars, key=lambda c: c.trip)
print(f"\nVoittaja on {voittaja.name} ({voittaja.top_speed} km/h), ajettu matka: {voittaja.trip:.1f} km")
