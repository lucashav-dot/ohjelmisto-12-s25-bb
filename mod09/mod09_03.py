class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        self.top_speed = 142
        self.register_number = "ABC-123"
    def accelerate1(self):
        self.speed += 30
    def current_speed(self):
        if self.speed < 0:
            self.speed = 0
        elif self.speed > 142:
            self.speed = self.top_speed
        return self.speed
    def time(self, time):
        self.time += time
    def trip_length(self, time):
        self.trip += self.speed * time
        return self.trip

car1 = Car()
car1.accelerate1()
car1.current_speed()
car1.trip_length(2)

print(f"Auton {car1.register_number} nopeus on: {car1.speed}km/h, huippunopeus: {car1.top_speed}km/h "
      f"ja kuljettu matka {car1.trip}km")