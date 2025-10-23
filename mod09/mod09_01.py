class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        self.top_speed = 142
        self.register_number = "ABC-123"
    def accelerate(self):
        self.speed += 1

cars = []
for i in range(5):
    cars.append(Car())
car1 = Car()
car1.accelerate()
car1.accelerate()
car2 = Car()
car1 = Car()

print(f"Auton {car1.register_number} nopeus on: {car1.speed}km/h, huippunopeus: {car1.top_speed}km/h "
      f"ja kuljettu matka {car1.trip}km")

cars[0].accelerate()
# Tulostetaan kaikkien autojen nopeudet
for car in cars:
    print(f"Auton nopeus: {car.speed}")