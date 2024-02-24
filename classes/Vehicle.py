class Vehicle:
    def __init__(self, max_speed, mileage, color="white"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.seatCap = None

    def assignSeatCapacity(self, seatCap):
        self.seatCap = seatCap

    def displayProperties(self):
        print("color", self.color)
        print("mileage", self.mileage)
        print("speed", self.max_speed)
        print("Seat capacity", self.seatCap)


vehicle1 = Vehicle(400, 20)
vehicle1.assignSeatCapacity(5)
vehicle1.displayProperties()
print()
vehicle2 = Vehicle(350, 10, "black")
vehicle2.assignSeatCapacity(7)
vehicle2.displayProperties()
