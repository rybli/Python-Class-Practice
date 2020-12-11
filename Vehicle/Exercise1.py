# Exercise Question 1: Create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def __repr__(self):
        return "A vehicle with {max_speed} max speed and {mileage} miles.".format(max_speed=self.max_speed,
                                                                                  mileage=self.mileage)


v1 = Vehicle(200, 1000)
print(v1)
