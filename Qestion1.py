class Vehicle:
    def describe(self):
        return "This is a vehicle."

class Car(Vehicle):
    def describe(self):
        return "This is a car."

class Bike(Vehicle):
    def describe(self):
        return "This is a bike."

# Example usage:
vehicle = Vehicle()
car = Car()
bike = Bike()

print(vehicle.describe())  # Output: This is a vehicle.
print(car.describe())      # Output: This is a car.
print(bike.describe())