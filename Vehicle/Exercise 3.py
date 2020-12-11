# Exercise Question 3: Create child class Bus that will inherit all of the
# variables and methods of the Vehicle class.


# Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __repr__(self):
        return "Vehicle Name: {name}\nSpeed: {speed}\nMileage: {mileage}".format(name=self.name,
                                                                                 speed=self.max_speed,
                                                                                 mileage=self.mileage)


b1 = Bus("School Volvo", 180, 12)
print(b1)