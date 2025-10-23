class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        self.top_speed = 142
        self.register_number = "ABC-123"
    def accelerate1(self):
        self.speed += 30
    def accelerate2(self):
        self.speed += 70
    def accelerate3(self):
        self.speed += 50
    def accelerate4(self):
        self.speed -= 200
    def current_speed(self):
        if self.speed < 0:
            self.speed = 0
        elif self.speed > 142:
            self.speed = self.top_speed
        return self.speed


car1 = Car()
car1.accelerate1()
car1.accelerate2()
car1.accelerate3()
car1.current_speed()

print(f"Auton {car1.register_number} nopeus on: {car1.speed}km/h, huippunopeus: {car1.top_speed}km/h.")
car1.accelerate4()
car1.current_speed()

print(f"Auton {car1.register_number} nopeus on: {car1.speed}km/h, huippunopeus: {car1.top_speed}km/h.")