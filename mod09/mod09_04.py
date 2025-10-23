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
    def trip_length(self):
        self.trip += self.speed


cars = []
for i in range(1, 11):
    car = Car(i)
    cars.append(car)

winner = None
tunti = 0
while not winner:
    tunti += 1
    print(f"Tunti: {tunti}")

    for car in cars:
        car.accelerate()
        car.trip_length()
        print(f"Auton {car.name} nopeus on {car.speed}km/h ja ajettu matka {car.trip}km")
        if car.trip >= 10000:
            winner = car
            input("Paina enter...")
            break

print(f"\nVoittaja oli {winner.name} huippunopeudella: {winner.top_speed}km/h ajettumatka: {winner.trip}km\n")
input("Paina enter...")
print("\nKaikkien autojen tulokset:")
for car in cars:
    print(f"Auton {car.name} huppunopeus:"
          f" {car.top_speed}km/h ajettumatka: {car.trip}km")