# Exercise Question 5: Define property that should have the same value for every class instance

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.


class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __repr__(self):
        return f"Color: {self.color} Name: {self.name} Max Speed: {self.max_speed} Mileage: {self.mileage}"


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


v1 = Vehicle("V1", 100, 10)
b1 = Bus("B1", 200, 20)
c1 = Car("C1", 300, 30)

print(v1)
print(b1)
print(c1)