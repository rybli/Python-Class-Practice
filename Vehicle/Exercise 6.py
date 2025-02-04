# Exercise Question 6: Class Inheritance

# Given:

# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50.
# So the final fare amount should be 5550.
# You need to override the fare() method of a Vehicle class in Bus class.

# Use the following code for your parent Vehicle class.
# We need to access the parent class from inside a method of a child class.


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        fare = super(Bus, self).fare()
        fare += fare * 10 / 100 # 10% tax
        return fare


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())